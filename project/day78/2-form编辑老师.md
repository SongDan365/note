### form编辑老师
views.py
```py
from django.shortcuts import render, redirect
from django.views import View
from django.forms import Form, fields, widgets  # widgets是个插件
from app01 import models

class EditTeacher(View):
    def get(self, request, tid):
        teacher = models.Teacher.objects.filter(id=tid).first()
        cls_ids = teacher.c2t.values_list("id")
        # cls_id_list = [ cls_id[0] for cls_id in cls_ids ]
        cls_id_list = list(zip(*cls_ids))[0] if list(zip(*cls_ids)) else []
        print(cls_id_list)
        obj = TeacherForm(initial={"tname": teacher.tname, "xx": cls_id_list})  # 初始化
        return render(request, "edit_teacher.html", {"obj": obj})
```

edit_teacher.html
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>编辑老师</h1>
        <form action="/edit_teacher/" method="post">
            {% csrf_token %}
            {{ obj.tname }} {{ obj.errors.tname.0 }}
            {{ obj.xx }}
            <input type="submit" value="提交"/>
        </form>
    </body>
</html>
```
