### Django程序目录
```
/mysite
    /mysite
        settings.py  # Django配置文件
        url.py       # 路由系统：url->函数
        wsgi.py      # 用于定义Django用什么socket, 测试用wsgiref,生产用uwsgi
```

### 第一个django请求
urls.py
```python
from django.urls import path
from django.shortcuts import HttpResponse

def login(request):
    # request 用户请求所有信息
    return HttpResponse("login")
    
urlpatterns = [
    path('login', login)
]
```
