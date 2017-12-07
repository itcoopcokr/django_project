## Github 설정 

~~~
git init
git add .
git commit -m "first commit"
git remote add origin git@github.com:itcoopcokr/django_project.git
git push -u origin master
~~~
- 참고 
~~~
git remote add itcoop_django git@github.com:itcoopcokr/django_project.git
git push itcoop_django 
~~~

<br/>

## 커맨드 라인
- 커맨드 라인에서 django_project 폴더로 이동 
~~~
cd django_project해당하는 폴더로 이동  
~~~

- 가상환경으로 실행 
~~~
django_projet $ Scripts\activate
~~~

- 가상환경 빠져 나오기 
~~~
(django_project) $ deactivate
~~~

- 새로운 패키지 실행 
    - Django 설치 
~~~
(django_project) $ pip install django==1.10
~~~
- 현재 파이썬 패키지 설치 리스트 
~~~
(django_project) $ pip freeze 

Django==1.10
~~~

- 현재 파이썬 패키지 리스트 정리
    - requirements.txt 파일 생성  
~~~
(django_project) $ pip freeze >> requirements.txt
~~~

- 현재 패키지 인스톨 
~~~
(django_project) $ pip install -r requirements.txt
~~~
 
<br/>

## .gitignore 파일 생성 
~~~
# Created by https://www.gitignore.io/api/pycharm,python,django

### Django ###
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
db.sqlite3
media

.idea
.idea/
.idea/*
.DS_Store
~~~