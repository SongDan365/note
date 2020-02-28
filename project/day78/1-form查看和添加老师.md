### form查看和添加老师
urls.py
```py
from django.contrib import admin
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path('teacher/', views.Teacher.as_view()),
    path('add_teacher/', views.AddTeacher.as_view()),
]
```

views.py
```py
from django.shortcuts import render, redirect
from django.views import View
from django.forms import Form, fields, widgets  # widgets是个插件
from app01 import models

class Teacher(View):
    def get(self, request):
        teacher_list = models.Teacher.objects.all()
        for teacher in teacher_list:
        return render(request, "teacher.html", {"teacher_list": teacher_list})

class TeacherForm(Form):
    tname = fields.CharField()
    # 多选form
    xx = fields.MultipleChoiceField(
        # 有__init__方法，这个就没有必要写了
        # choices = models.Classes.objects.values_list("id", "title"),
        widget = widgets.SelectMultiple
    )

    # 解决添加班级不能及时更新的问题
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["xx"].choices = models.Classes.objects.values_list("id", "title")

class AddTeacher(View):
    def get(self, request):
        obj = TeacherForm()
        return render(request, "add_teacher.html", {"obj": obj})

    def post(self, request):
        obj = TeacherForm(request.POST)
        if obj.is_valid():
            xx = obj.cleaned_data.pop("xx")
            row = models.Teacher.objects.create(**obj.cleaned_data)
            row.c2t.add(*xx)
            return redirect("/teacher/")
        return render(request, "add_teacher.html", {"obj": obj})
```

teacher.html
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>老师列表</h1>
        <a href="/add_teacher/">添加老师</a>
        <table border="1">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>姓名</th>
                    <th>任教班级</th>
                </tr>
            </thead>
            <tbody>
                {% for teacher in teacher_list %}
                    <tr>
                        <td>{{ teacher.id }}</td>
                        <td>{{ teacher.tname }}</td>
                        <td>
                            {% for class in teacher.c2t.all %}
                                {{ class.title }}
                            {% endfor %}
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
</html>
```

add_teacher.html
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>添加老师</h1>
        <form action="/add_teacher/" method="post" novalidate>
            {% csrf_token %}
            <p>{{ obj.tname }} {{ obj.name.errors.0 }}</p>
            <p>{{ obj.xx }} {{ obj.xx.errors.0 }}</p>
            <input type="submit" value="提交"/>
        </form>
    </body>
</html>
```
