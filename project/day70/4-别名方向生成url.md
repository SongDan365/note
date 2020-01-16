### 别名反生成url
urls.py
```py
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path("index/", views.index, name="n1"),
    re_path('index/(\w+)', views.index, name="n1"),
]
```

views.py
```py
from django.shortcuts import render, HttpResponse
from django.urls import reverse

def index(request, *args, **kwargs):
    path = reverse("n1")
    path = reverse("n1", args=(456,))
    path = reverse("n1", kwargs={"aaa": 111})
    return HttpResponse(path)
```

index.html
```html
<!doctype html>
<html>
    <a href="{% url 'n1' %}">

    <a href="/index/{{ class.id }}/">
    <a href="{% url 'n1' class.id %}"> <!-- 和上面一样 -->
    <a href="{% url 'n1' class.id teacher.id %}"> <!-- 和上面一样 -->
    </a>
</html>
```
