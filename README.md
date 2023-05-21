# 프로젝트 개요
#### 공개되어 있는 쇼핑몰 데이터를 처리하는 ETL 파이프라인을 구축하고 파이프라인에 장애가 일어난 경우에 대응할 수 있는 복구 자동화를 구현한다.

# 프로젝트 목표
#### 1. ETL 파이프라인을 구축해본다.
#### 2. ETL 파이프라인을 디버깅하는 방법을 학습한다.
#### 3. ETL 파이프라인이 실패한 경우 자동으로 복구를 하는 법을 학습한다.

# 프로젝트 사용 자료
#### 온라인 리테일 사이트의 2010년 12월~2011년 12월간의 주문 기록 데이터 (약 50만건) [링크](https://archive.ics.uci.edu/ml/datasets/Online+Retail)

# 프로젝트 목차
#### 1. 로컬 머신에서 Apache Airflow 환경설정
#### 2. Apache Airflow 이해
#### 3. 공식 튜토리얼 살펴보기
#### 4. 과제 1: 일별 데이터 가져와서 로컬 머신에 저장하는 Task 만들어 보기
#### 5. 과제 2: 데이터를 가공해서 저장하는 Task들 만들어보기
#### 6. 과제 3: 로그 데이터를 가져와서 저장하는 Task 만들어 보기
#### 7. 과제 4: 과제 2의 구매 금액이 큰 사용자 top 3에 대해서 과제 3의 Task를 이용해서 관련 데이터를 추출하고 텍스트 형식의 보고서를 만드는 workflow 만들어 보기 / REST api를 이용해 실행할 수 있도록 해보기
#### 8. Apache Airflow 디버깅 하는 법 알아보기
#### 9. 과제 5: 장애가 난 경우에 사용할 수 있는 백필 workflow 구현해 보기 / REST api를 이용해 실행할 수 있도록 해보기

# 목차별 설명
## 1. Window 로컬 머신에서 Apache Airflow 환경설정 방법
### A. Windows 에 Docker 설치하기
####  a. [Doker Download Link](https://docs.docker.com/desktop/windows/install)
####  b. [wsl2 설치 참고](https://docs.microsoft.com/ko-kr/windows/wsl/install-manual)
####  c. Ubuntu 22.04 LTS 설치하기 (Microsoft Store)
####  d. Doker 아이콘 우클릭 후 Switch to Linux containers... 를 클릭

### B. Doker 내 Airflow 설치하기
#### a. pip3 설치하기
 a) apt를 업데이트 한 뒤 pip3를 설치한다.
 ```ubuntu
 sudo apt update && sudo apt install python3-pip
 ```
 b) pip3 설치 여부 확인
 ```ubuntu
 pip3 --version
 ```
 c) airflow 라이브러리를 설치한다.
 ```ubuntu
 pip3 install apache-airflow
 ```
 #### b. workspace 구성
 a) 홈 디렉토리에서 airflow 전용 workspace를 만듦
 ```ubuntu
 mkdir -p airflow/{dags,logs,plugins}
 ```
 b) 설정 파일 생성
 ```ubuntu
 cd airflow
 id
 echo -e "AIRFLOW_UID=$(id -u)" > .env
 ```
 c) Doker 설정
 
 ## 2. Apache Airflow 이해
 ### [Apahce Airflow 참고자료](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html)
 ## 3. 공식 튜토리얼 살펴보기
 ### [공식 튜토리얼 참고자료](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html)
 
 ## 4. 과제 1: 일별 데이터 가져와서 로컬 머신에 저장하는 Task 만들어 보기
 ### 과제 내용 : 
 #### 특정 일자의 데이터를 가져오는 Task 만들기
 
 ## 5. 과제 2: 데이터를 가공해서 저장하는 Task들 만들어보기
 ### 과제 내용 : 
 #### a. 지역별로 해당 일자에 가장 많이 팔린 상품 top 30
 #### b. 지역별로 해당 일자에 구매 금액 큰 사용자 top 3
 #### c. 판매 금액으로 정렬한 지역 top 5
 #### d. 과제 1의 Task가 과제 2의 Task를 실행하도록 변경해보기


 
