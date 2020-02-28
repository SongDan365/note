### 伪ajax
urls.py
```py
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path("fake_ajax/", views.FakeAjax.as_view()),
]
```

views.py
```py
from django.shortcuts import render, redirect, HttpResponse
from django.views import View

class FakeAjax(View):
    def get(self, request):
        return render(request, "fake_ajax.html")

    def post(self, request):
        print(request.POST)
        return HttpResponse("...")
```

fake_ajax.html
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <!-- target指定提交给谁 -->
        <form id="f1" method="post" target="ifr">
            {% csrf_token %}
            <iframe id="ifr" name="ifr" style="display: none"></iframe>
            <input name="user"/>
            <a onclick="submitForm()">提交</a>
        </form>
        <script>
            function submitForm(){
                document.getElementById("ifr").onload = loadIframe;
                document.getElementById("f1").submit();
            }
            function loadIframe(){
                /* 获取返回值 */
                var content = document.getElementById("ifr").contentWindow.document.body.innerText
                alert(content)
            }
        </script>
    </body>
</html>
```
