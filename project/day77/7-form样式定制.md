### form样式定制
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
    name = fields.CharField(
        widget=widgets.TextInput(attrs={"class": "form-control"})  # 自定义生成的input标签的属性
    )
    email = fields.EmailField(widget=widgets.TextInput(attrs={"class": "form-control"}))
    age = fields.IntegerField(min_value=18, max_value=25, widget=widgets.TextInput(attrs={"class": "form-control"}))
    cls_id = fields.IntegerField(
        widget=widgets.Select(choices=models.Classes.objects.values_list("id", "title"), attrs={"class": "form-control"})    # 使用select插件，choices=[(1, "北京"), (2, "上海")]
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

edit_student.html
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="/static/bootstrap/css/bootstrap.css"/>
    </head>
    <body>
        <h1>编辑学生</h1>
        <div style="width: 500px; margin:0 auto;">
            <form class="form-horizontal" action="/edit_student/{{ nid }}/" method="post" novalidate>
                {% csrf_token %}
                <div class="form-group">
                    <label for="inputEmail3" class="col-sm-2 control-label">姓名</label>
                    <div class="col-sm-10">
                        {{ obj.name }}
                    </div>
                </div>
                <div class="form-group">
                    <label for="inputPassword3" class="col-sm-2 control-label">邮箱</label>
                    <div class="col-sm-10">
                        {{ obj.email }} {{ obj.errors.email.0 }}
                    </div>
                </div>
                <div class="form-group">
                    <label for="inputPassword3" class="col-sm-2 control-label">年龄</label>
                    <div class="col-sm-10">
                        {{ obj.age }} {{ obj.errors.age.0 }}
                    </div>
                </div>
                <div class="form-group">
                    <label for="inputPassword3" class="col-sm-2 control-label">班级</label>
                    <div class="col-sm-10">
                        {{ obj.cls_id }} {{ obj.errors.cls_id.0 }}
                    </div>
                </div>
                <div class="form-group">
                    <div class="col-sm-offset-2 col-sm-10">
                    <button type="submit" class="btn btn-default">提交</button>
                    </div>
                </div>
            </form>
        </div>
    </body>
</html>
```
