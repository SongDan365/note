### cbv
urls.py
```py
from django.urls import path
from app01 import views

urlpatterns = [
    path("index/", views.Index.as_view()),
]
```

views.py
```py
from django.shortcuts import render, HttpResponse
from app01 import models
from django.views import View

class Index(View):
    """
    get     查
    post    增
    put     更新
    delete  删
    """

    def dispatch(self, request, *args, **kwargs):
        """
        程序进来会先执行这个方法，在执行get 或post方法。
        如果想要对这个url进行批量操作，可以在这个方法里写程序
        """
        obj = super().dispatch(request, *args, **kwargs)
        return obj

    def get(self, request, *args, **kwargs):
        return HttpResponse("Index.get")

    def post(self, request, *args, **kwargs):
        return HttpResponse("Index.post")
```
