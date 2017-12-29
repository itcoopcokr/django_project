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
- /contact/models.py
    - 날짜,시간추가 
    - 추가 : timestamp = models.DateTimeField(auto_now_add=True)
~~~
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
~~~  
- DB 업데이트 
~~~
$ python manage.py makemigrations

You are trying to add the field 'timestamp' with 'auto_now_add=True' to contact without a default; the database needs something to populate existing rows.

 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
[default: timezone.now] >>> timezone.now
Migrations for 'contact':
  contact/migrations/0002_contact_time
~~~
~~~
$ python manage.py migrate
~~~

- 사용자가 contact 보낼 때 입력
    - /contact/views.py
~~~
from django.shortcuts import render

from django.views.generic import CreateView, TemplateView

from .models import Contact
from .forms import ContactForm

# Create your views here.
class ContactCreateView(CreateView):
    model = Contact
    template_name = 'landingpage.html'
    success_url = '/contact/done'
    form_class = ContactForm
~~~
- 폼 구성 
    - /contact/forms.py
~~~
from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'message'
        ]
~~~  
- contact 완료 메세지 
    - /contact/views.py
~~~
class ContactDoneView(TemplateView):
    template_name = 'contact_done.html'
~~~
- /templates/
    - 추가 : contact_done.html
~~~
{% extends 'base.html' %}

{% block content %}

<br><br><br>

<div class="container">
    <div class="row">
        <div class="col-sm-12">

            <h1>메세지가 접수됐습니다.</h1>
            <p><a href="/" class="btn btn-secondary" role="button">Home</a> </p>

        </div>
    </div>
</div>

{% endblock %}
~~~    

## 이동경로 urls

- /mysite/urls.py
    - contact.urls
~~~
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'accounts/register/done/$', UserCreateDoneView.as_view(), name='register_done'),
    url(r'^$', Home.as_view()),
    url(r'^base/$', Base.as_view()),
    url(r'^team/$', Team.as_view()),
    url(r'^index/$', Landingpage.as_view()),
    url(r'^videos/$', VideoListView.as_view(), name='videos'),
    url(r'^videos/(?P<pk>\d+)/$',VideoDetailView.as_view(), name='video-detail'),
    url(r'^videos/create/$', VideoCreateView.as_view(), name='video-create'),
    url(r'^videos/(?P<pk>\d+)/update/$', VideoUpdateView.as_view(), name='video-update' ),
    url(r'^videos/(?P<pk>\d+)/delete/$', VideoDeleteView.as_view(), name='video-delete' ),
    url(r'^photo/', include('photo.urls', namespace='photo')),
    url(r'^board/', include('board.urls', namespace='board')),
    url(r'^contact/', include('contact.urls', namespace='contact')),
]                      
~~~
- /contact/urls.py
~~~
from django.conf.urls import url

from .views import ContactCreateView, ContactDoneView

urlpatterns = [
    url(r'^create/$',ContactCreateView.as_view(), name='create'),
    url(r'^done/$',ContactDoneView.as_view(), name='done')
]
~~~
- landingpage.html
    - form 내용 
~~~
    <h3>Contact Us</h3>
    {% if form.errors %}
    <div class="alert alert-danger" role="alert">
        {{ form.errors }}
    </div>
    {% endif %}
    <form method="post" action="/contact/create/">{% csrf_token %}
        <input type="text" name="name" placeholder="Full Name" class="form-control" required>
        <input type="email" name="email" placeholder="Email" class="form-control" required>
        <textarea rows="5" name="message" placeholder="Message..." class="form-control" required></textarea>

        <div id="send-btn">
            <button type="submit" class="btn btn-lg btn-general">SEND</button>
        </div>

    </form>
~~~                        

    
    