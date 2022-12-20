import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()  # 최대화

# 1. 페이지 이동
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)

# 2. 조회 항목 초기화 (체크 해제)
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()  # 클릭 (체크 해제)

# 3. 조회 항목 설정
items_to_select = ['영업이익', '자산총계', '매출액']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..')  # 부모 element (td)
    label = parent.find_element(By.TAG_NAME, 'label')
    if label.text in items_to_select:
        checkbox.click()

# 4. 적용하기 클릭
btn_apply = browser.find_element(
    By.XPATH, '//a[@href="javascript:fieldSubmit()"]')  # a 태그의 href 속성값으로 XPATH
btn_apply.click()


for idx in range(1, 40):  # 1 이상 40 미만 페이지 반복
    # 사전 작업 : 페이지 이동
    browser.get(url + str(idx))

    # 5. 데이터 추출
    df = pd.read_html(browser.page_source)[1]

    # row 단위, 결측치가 모든 row에 있을경우 삭제
    df.dropna(axis='index', how='all', inplace=True)
    df.dropna(axis='columns', how='all', inplace=True)
    if len(df) == 0:  # 더 이상 가져올 데이터가 없다면?
        break

    # 6. 파일 저장
    f_name = 'stock.csv'
    # 처음 저장 시 헤드 부분 포함, 그 후에는 헤드 부분 제외해야 하므로 파일 유무 확인하기
    if os.path.exists(f_name):  # 파일이 존재한다면 (헤더 제외)
        df.to_csv(f_name, encoding='utf-8-sig', index=False,
                  mode='a', header=False)  # mode ='a' > append
    else:  # 파일이 없다면 (헤더 포함)
        df.to_csv(f_name, encoding='utf-8-sig', index=False)
    print(f'{idx} 페이지 완료')

browser.quit()
