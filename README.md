# python_web_crawling

VS 파이썬 가상환경을 이용하여 진행
![image](https://user-images.githubusercontent.com/99489461/208561015-89f2d336-b0db-4510-ab9e-38a16456b548.png)

가상환경으로 바꾼 후 pip install pandas, selenium 으로 설치

* 실행 시 해당 오류가 뜰 경우 크롬 버전에 맞는 크롬 드라이버를 설치하여 기존 크롬 드라이버에 덮어쓰기
(크롬 드라이버 홈페이지 : https://chromedriver.chromium.org/downloads)
![image](https://user-images.githubusercontent.com/99489461/208560781-f38cf660-4414-4aa6-9be2-645edbc4bcce.png)


naverstock.py

실행시 
1. 자동으로 크롬 실행 후 최대화
2. 네이버 증권 사이트의 국내증시 탭에서 '영업이익', '자산총계', '매출액' 항목을 선택하여 조회
3. 1~39페이지까지의 정보들을 .csv 파일로 저장합니다.
![image](https://user-images.githubusercontent.com/99489461/208561375-759bf6cc-f63a-4d8e-8888-c34882ed3049.png)

naverairport.py

실행시
1. 자동으로 크롬 실행 후 최대화
2. 네이버 항공권 사이트의 가는 날과 오는 날을 선택(해당 코드는 12월 31일과 1월 1일로 선택)
3. 도착지 선택(해당 코드는 제주도로 설정하였습니다.)
4. 항공권 검색을 선택하여 항공권 결과가 나올 때까지 대기
5. 결과의 최상단(출발시각 빠른 순) 정보 print 문으로 출력
![image](https://user-images.githubusercontent.com/99489461/208562185-734a416a-3640-4e4a-bb00-922b271ea75d.png)
