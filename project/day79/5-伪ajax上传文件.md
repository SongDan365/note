### 伪ajax上传文件
urls.py
```py
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path("upload/", views.Upload.as_view()),
]
```

views.py
```py
from django.shortcuts import render, redirect, HttpResponse
from django.views import View

class Upload(View):
    def get(self, request):
        return render(request, "upload.html")

    def post(self, request):
        print(request.POST)
        print(request.FILES)
        file_obj = request.FILES.get("fafafa")
        import os
        file_path = os.path.join("static", file_obj.name)
        with open(file_path, "wb") as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
        return HttpResponse(file_path)
```

upload.html
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>伪ajax上传文件</h1>
        <form method="post" target="ifr" id="f1" enctype="multipart/form-data">
            {% csrf_token %}
            <iframe id="ifr" name="ifr" style="display: none"></iframe>
            <input type="file" id="i1" name="fafafa"/>
        </form>
        <a onclick="upload1()">上传</a>
        <div id="img1">
        </div>
        <script>
            function upload1(){
                document.getElementById("ifr").onload = loadIframe;
                document.getElementById("f1").submit();
            }

            function loadIframe(){
                var content = document.getElementById("ifr").contentWindow.document.body.innerText;
                var tag = document.createElement("img");
                tag.src= "/" + content;
                document.getElementById("img1").appendChild(tag);
            }
        </script>
    </body>
</html>
```
