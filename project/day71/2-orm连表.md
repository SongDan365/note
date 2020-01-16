### orm连表
views.py
```py
from django.shortcuts import HttpResponse
from app01 import models

def test(request):
    result = models.UserInfo.objects.all()  # reutrn Q[obj, obj, obj]
    for obj in result:
        obj.ut.title  # 用obj正向连表
        obj.ut.fo.caption  # 连多个表

    obj = models.UserType.objects.first()
    obj.userinfo_set.all()  # obj反向连表，一对多

    models.UserInfo.objects.values("id", "name")  # return Q[{"id": 1, "name": "aaa"}, {"id": 2, "name": "bbb"}, {"id": 3, "name": "ccc"}]
    models.UserInfo.objects.values_list("id", "name")  # return Q[(1, "aaa"), (2, "bbb"), (3, "ccc")]


    models.UserInfo.objects.values("ut__title")  # 取值时，正向连表
    models.UserType.objects.values("userinfo__name")  # 取值时，反向连表



    return HttpResponse("...")
```
