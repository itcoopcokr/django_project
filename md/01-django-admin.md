## 장고 프로젝트 생성 
~~~
$ django-admin.py startproject mysite
~~~

- 프로젝트 명을 source로 변경 
~~~
/source/
    /mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    manage.py
~~~    


<br>
- 장고 서버 실행 
~~~
$ python manage.py runserver
~~~

- http://localhost:8000

<br/>
    

- DB 생성 
~~~    
$ python manage.py makemigrations
$ python manage.py migrate 
~~~

<br/>

- 슈퍼유저 생성 
~~~
$ python manage.py createsuperuser
username : admin
email : a@a.com
password : admin1234
~~~

<br/>

- 장고 서버 실행 
~~~
$ python manage.py runserver
~~~

- admin 관리자 보기 
    - http://localhost:8000/admin/
    


    
