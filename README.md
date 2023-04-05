# 1. Windows 에 Docker 설치하기
 ### 1. [Doker Download Link](https://docs.docker.com/desktop/windows/install)
 ### 2. [wsl2 설치 참고](https://docs.microsoft.com/ko-kr/windows/wsl/install-manual)
 ### 3. Ubuntu 22.04 LTS 설치하기 (Microsoft Store)
 ### 4. Doker 아이콘 우클릭 후 Switch to Linux containers... 를 클릭

# 2. Doker 내 Airflow 설치하기
 ### 1. pip3 설치하기
 1) apt를 업데이트 한 뒤 pip3를 설치한다.
 ```ubuntu
 sudo apt update && sudo apt install python3-pip
 ```
 2) pip3 설치 여부 확인
 ```ubuntu
 pip3 --version
 ```
 3) airflow 라이브러리를 설치한다.
 ```ubuntu
 pip3 install apache-airflow
 ```
  ### 2. workspace 구성
 1) 홈 디렉토리에서 airflow 전용 workspace를 만듦
 ```ubuntu
 mkdir -p airflow/{dags,logs,plugins}
 ```
 2) 설정 파일 생성
 ```ubuntu
 cd airflow
 id
 echo -e "AIRFLOW_UID=$(id -u)" > .env
 ```
 3) Doker 설정
 
