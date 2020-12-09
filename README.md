# Django Quick Start
### 1. 가상화 설치
    > python3 -m venv venv

### 2. django 설치
    > python -m pip install Django

### 3. django 설치 확인
    > python3
    >> import django

### 4. django 버전 확인
    > python3 -m django --version

### 5. 가상화 실행
    > source venv/bin/activate
    
### 6. 파일 구동
    > cd devmap
    > python3 manage.py runserver
### 7. 외부(AWS) 환경에서 구동
    > python3 manage.py runserver 0.0.0.0:8000

# Nginx restart
    1. uwsgi setup
       > uwsgi --ini uwsgi.ini
    2. sudo service nginx restart or sudo /etc/init.d/nginx restart

# pip info
### pip package
    > pip freeze
### pip save
    > pip freeze > requirements.txt
### pip reload
    > pip install -r requirements.txt