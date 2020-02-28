### jquery ajax上传文件
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
        <h1>原生ajax上传文件</h1>
        <input type="file" id="i1"/>
        <a onclick="upload1()">上传</a>
        <div id="img1">
        </div>
        <script src="/static/jquery.js"></script>
        <script>
            function upload1(){
                /* 这个对象可以传字符串也可以传文件 */
                var formData = new FormData();
                formData.append("k1", "v1");
                /* jquery_obj[0] 是dom对象 */
                formData.append("fafafa", $("#i1")[0].files[0]);
                $.ajax({
                    url: "/upload/",
                    type: "post",
                    data: formData,
                    headers: {"X-CSRFToken": "{{ csrf_token }}"},
                    contentType: false,
                    processData: false,
                    success: function(arg){
                        var tag = document.createElement("img");
                        tag.src = "/" + arg;
                        $("#img1").append(tag);
                    }
                })
            }
        </script>
    </body>
</html>
```
