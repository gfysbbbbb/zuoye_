#老师，每一次我做的修改都记录在手机的备忘录上了

登陆git点击new
使用public
点击创建
使用ssh
配置证书
git bash输入：ssh-keygen
                           默认地址
                           cat～/.ssh/id_rsa.pub
                           ls ～/.ssh/
                           显示：id_ras  id_ras. pub
将 ~/.ssh/id_rsa.pub文件的内容复制到git服务器的ssh keys
进入仓库，克隆仓库
git建目录 ：mkdir repos
                   cd repos
                   git clone git@github.com:gfysbbbbb/zuoye_.git
cd zuoye_
echo "作业">>readme. md
git status：untracked files
git add .
git status:changes
git commit -m "增加"
git push
Django开发
cmd:
Django-admin startproject mysite1
cd mysite1
python manage.py runserver 
localhost：8000 出现小火箭
CTR C退出
创建app：
python manage. py startapp polls
python manage. py startapp news
cd news
cd .. （注意不要建错位置）
VScode:
打开工作区zuoye_
将db pyc文件添加到gitignore
**.pyc
**.sqlite3
打开终端git status
git add . 
git commit -m "新的Django工程"
git push
将以下代码复制到models：
from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

终端：python manage.py makemigrations
python manage.py migrate
#后台管理页面加文章
admin: from django.contrib import admin
from . import models
admin.site.register(models.Article)
admin.site.register(models.Reporters)

终端 python manage. py createuperuser
python manage. py runserver
打开localhost:8000/admin
article
重启服务器

#设计URL前端页面
from django.urls import path

from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    #path('articles/<int:year>/<int:month>/', views.month_archive),
   # path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]

from django.shortcuts import render

from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

templates/news
year_archive. html

{% extends "base.html" %}
{% block title %}Articles for {{ year }}{% endblock %}
{% block content %}
<h1>Articles for {{ year }}</h1>
{% for article in article_list %}
    <p>{{ article.headline }}</p >
    <p>By {{ article.reporter.full_name }}</p >
    <p>Published {{ article.pub_date|date:"F j, Y" }}</p >
{% endfor %}
{% endblock %}
ach
注册
urls. py 
增加 path('news/',include(news.site.urls)，
base. html
{% load static %}
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    < img src="{% static 'images/sitelogo.png' %}" alt="Logo">
    {% block content %}{% endblock %}
</body>
</html>
运行查看结果

#作业
#models.py中的"Report""Article"改为"Student""Homework"
from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=70)
    
    def __str__(self):
        return self.full_name

class Homework(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

#建立html文件
templates/news
homework_form. html
<html>
<body>
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>
</body>
</html>

news/view.py
from.models import Student, Homework
 
from django.views.generic.edit import CreateView
 
class HomeworkCreate(CreateView):
    model = Homework
    template_name = 'homework_form.html'
    fields = ['headline','attach','remark','student']

news/urls.py
urlpatterns = [
    path('hw/create/', views.HomeworkCreate.as_view()),
#添加Student用户
news/admin.py
admin.site.register(models.Student)

#数据库迁移
python .\manage.py makemigrations
python .\manage.py migrate

#修改homework_form. html
<html>
<body>
<form method="post" enctype="multipart/form-data" >{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>
</body>
</html>

#创建根路径
news
urls. py
path('',include('news.urls'))
mysite
urls. py
path('', views.HomeworkCreate.as_view())

#运行服务器