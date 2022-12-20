from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
url = 'https://flight.naver.com/'
browser.get(url)
browser.maximize_window()

time.sleep(2)

#
one_month = browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[8]/div/div[2]/button[1]')
one_month.click()

begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_date.click()

time.sleep(1)

day31 = browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[8]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[7]/button')
day31.click()

day1 = browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/button')
day1.click()

arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
arrival.click()

time.sleep(1)

domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]')
domestic.click()

time.sleep(2)

jeju = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]')
jeju.click()

time.sleep(2)

search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
search.click()

elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located(
    (By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
print(elem.text)
