## Contact 어플리케이션 만들기 
- 콘솔에서 "contact" 어플리케이션 만들기 
~~~
$ python manage.py startapp contact
~~~
- /mysite/setting.py
    - intall_app
    - 추가 : 'contact',
~~~
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'videos',
    'photo',
    'board',
    'contact',
]
~~~
- Contact DB 생성 
    - name
    - email 
    - message 
- /contact/models.py
~~~
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
~~~            
- 파이썬 코드로 DB 적용 가능한 파일 생성
~~~
$ python manage.py makemigrations
~~~

- 실제 DB 적용 
~~~
$ python manage.py migrate
~~~

- 관리자에서 볼수 있게 
    - /contact/admin.py
~~~
from django.contrib import admin

# Register your models here.
from .models import Contact

# class ContactAdmin(admin.ModelAdmin):

admin.site.register(Contact)
~~~
- 관리자화면(객체)에서 이름이 나오게
    - 추가 : def __str__(self):
~~~
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name 
~~~
- 관리자 리스트에 이름,이메일 보이게 
~~~
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email')

admin.site.register(Contact,ContactAdmin )
~~~
    