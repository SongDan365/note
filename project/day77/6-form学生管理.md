### form学生管理
urls.py
```py
from django.contrib import admin
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path('student/', views.StudentList.as_view()),
    path('add_student/', views.AddStudent.as_view()),
    re_path('edit_student/(\d+)/', views.EditStudent.as_view()),
]
```

views.py
```py
from django.shortcuts import render, redirect
from django.views import View
from django.forms import Form, fields, widgets  # widgets是个插件
from app01 import models

class StudentList(View):
    def get(self, request):
        student_list = models.Student.objects.all()
        return render(request, "student_list.html", {"student_list": student_list})

class StudentForm(Form):
    name = fields.CharField()
    email = fields.EmailField()
    age = fields.IntegerField(min_value=18, max_value=25)
    cls_id = fields.IntegerField(
        widget=widgets.Select(choices=models.Classes.objects.values_list("id", "title"))    # 使用select插件，choices=[(1, "北京"), (2, "上海")]
    )

class AddStudent(View):
    def get(self, request):
        obj = StudentForm()
        return render(request, "add_student.html", {"obj": obj})

    def post(self, request):
        obj = StudentForm(request.POST)
        if obj.is_valid():
            models.Student.objects.create(**obj.cleaned_data)
            return redirect("/student/")
        return render(request, "add_student.html", {"obj": obj})

class EditStudent(View):
    def get(self, request, nid):
        student = models.Student.objects.filter(id=nid).values("name", "email", "age", "cls_id").first()  # 获取字典形式的数据库值
        obj = StudentForm(initial=student)
        return render(request, "edit_student.html", {"obj": obj, "nid": nid})

    def post(self, request, nid):
        obj = StudentForm(request.POST)
        if obj.is_valid():
            models.Student.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect("/student/")
        return render(request, "edit_student.html", {"obj": obj, "nid": nid})
```

add_student.html
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>添加学生</h1>
        <form action="/add_student/" method="post" novalidate>
            {% csrf_token %}
            <p>{{ obj.name }} {{ obj.errors.name.0 }}</p>
            <p>{{ obj.email }} {{ obj.errors.email.0}}</p>
            <p>{{ obj.age }} {{ obj.errors.age.0}}</p>
            <p>{{ obj.cls_id }} {{ obj.errors.cls_id.0}}</p>
            <input type="submit" value="提交"/>
        </form>
    </body>
</html>
```


models.py
```py
from django.db import models

# Create your models here.
class Classes(models.Model):
    title = models.CharField(max_length=32)

class Student(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    age = models.IntegerField()
    cls = models.ForeignKey("Classes", null=True, on_delete=models.SET_NULL)

class Teacher(models.Model):
    tname = models.CharField(max_length=32)
    c2t = models.ManyToManyField("classes")
```

edit_student.html
```py
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>编辑学生</h1>
        <form action="/edit_student/{{ nid }}/" method="post" novalidate>
            {% csrf_token %}
            <p>{{ obj.name }} {{ obj.errors.name.0 }}</p>
            <p>{{ obj.email }} {{ obj.errors.email.0}}</p>
            <p>{{ obj.age }} {{ obj.errors.age.0}}</p>
            <p>{{ obj.cls_id }} {{ obj.errors.cls_id.0}}</p>
            <input type="submit" value="提交"/>
        </form>
    </body>
</html>
```

student_list.html
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>学生列表</h1>
        <a href="/add_student/">添加学生</a>
        <ul>
            {% for student in student_list %}
            <li>{{ student.name }} - {{ student.email }} - {{ student.age }} - {{ student.cls_id }} - {{ student.cls.title }} <a href="/edit_student/{{ student.id }}/">编辑</a></li>
            {% endfor %}
        </ul>
    </body>
</html>
```
