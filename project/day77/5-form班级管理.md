### form查看添加编辑班级
urls.py
```py
from django.contrib import admin
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path('class/', views.ClassList.as_view()),
    path('add_class/', views.AddClass.as_view()),
    re_path('edit_class/(\d+)/', views.EditClass.as_view()),
]
```

views.py
```py
from django.shortcuts import render, redirect
from django.views import View
from django.forms import Form, fields
from app01 import models

class ClassForm(Form):
    title = fields.CharField()

class ClassList(View):
    def get(self, request):
        class_list = models.Classes.objects.all()
        return render(request, "class_list.html", {"class_list": class_list})

    def post(self, request):
        pass

class AddClass(View):
    def get(self, request):
        obj = ClassForm()
        return render(request, "add_class.html", {"obj": obj})
        
    def post(self, request):
        obj = ClassForm(request.POST)
        if obj.is_valid():
            models.Classes.objects.create(**obj.cleaned_data)
            return redirect("/class/")
        else:
            return render(request, "add_class.html", {"obj": obj})

class EditClass(View):
    def get(self, request, nid):
        class_info = models.Classes.objects.filter(id=nid).first()
        # obj = ClassForm({"title": class_info.title})  # 这么写会校验数据是否合理
        obj = ClassForm(initial={"title": class_info.title})  # 不校验数据
        return render(request, "edit_class.html", {"class_info": class_info, "obj": obj})

    def post(self, request, nid):
        obj = ClassForm(request.POST)
        if obj.is_valid():
            models.Classes.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect("/class/")
        else:
            return render(request, "edit_class.html", {"class_info": class_info, "obj": obj})
```

models.py
```py
from django.db import models

class Classes(models.Model):
    title = models.CharField(max_length=32)

class Student(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    age = models.IntegerField(max_length=32)
    cls = models.ForeignKey("Classes", null=True, on_delete=models.SET_NULL)

class Teacher(models.Model):
    tname = models.CharField(max_length=32)
    c2t = models.ManyToManyField("classes")

```

add_class.py
```py
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>添加班级</h1>
        <form action="/add_class/" method="post" novalidate>
            {% csrf_token %}
            {{ obj.title }} {{ obj.errors.title.0 }}
            <input type="submit" value="提交"/>
        </form>
    </body>
</html>
```

edit_class.py
```py
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>编辑班级</h1>
        <form action="/edit_class/{{ class_info.id }}/" method="post">
            {% csrf_token %}
            {{ obj.title }} {{ obj.errors.title.0 }}
            <input type="submit" value="提交"/>
        </form>
    </body>
</html>
```

class.html
```py
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>
            班级列表
        </h1>
        <a href="/add_class/">添加班级</a>
        <ul>
            {% for class in class_list %}
                <li>{{ class.title }} <a href="/edit_class/{{ class.id }}/">编辑</a></li>
            {% endfor %}
        </ul>
    </body>
</html>
```
