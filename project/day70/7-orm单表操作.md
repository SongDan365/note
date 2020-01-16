### orm单表操作
views.py
```py
from django.shortcuts import render, HttpResponse
from app01 import models

def index(request):
    # 添加数据
    models.UserGroup.objects.create(title="销售部")

    # 查
    group_list = models.UserGroup.objects.all()  # 查所有，返回[obj, boj]
    group_list[0].id  # 拿数据

    group_list = models.UserGroup.objects.filter(id=1, title="aaa")  # 条件查找，默认and
    group_list = models.UserGroup.objects.filter(id__gt=1, title="aaa")  # gt 大于, lt小于

    # 删除
    models.UserGroup.objects.filter(id=1).delete()

    # 更新
    models.UserGroup.objects.filter(id=1).update(title="aaa")
    return HttpResponse("...")
```
