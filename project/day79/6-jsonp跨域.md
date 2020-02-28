### jsonp跨域
```
ajax给别人的URL发请求就会有跨域问题

jsonp跨域原理
    1. 把数据放在html中
    2. 用<script>的src获取数据
    3. 自己定义一个list函数
    4. 请求的地址返回一个list("...")
```

urls.py
```py
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path("users/", views.Users.as_view()),
    path("jsonp/", views.Jsonp.as_view()),
]
```

views.py
```py
from django.shortcuts import render, redirect, HttpResponse
from django.views import View

class Users(View):
    def get(self, request):
        user_list = ["aaa", "bbb", "ccc"]
        funcname = request.GET.get("callback")
        import json
        user_list_str = json.dumps(user_list)
        temp = "%s(%s)" % (funcname, user_list_str)
        return HttpResponse(temp)

class Jsonp(View):
    def get(self, request):
        return render(request, "jsonp.html")
```

jsonp.html
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <input type="button" onclick="getUsers()" value="发送"/>
        <ul id="user_list">
        </ul>
        <!-- 原生jsonp
        <script>
            function getUsers(){
                var tag = document.createElement("script");
                tag.src = "/users/?callback=bbb";
                document.head.appendChild(tag);
            };
    
            function bbb(arg){
                console.log(arg);
            };


        </script>
        -->

        <!-- jquery jsonp -->
        <script src="/static/jquery.js"></script>
        <script>
            function getUsers(){
                $.ajax({
                    url: "/users/?callback=bbb",
                    type: "get",
                    dataType: "jsonp",
                    jsonp: "callback",
                    jsonpCallback: "bbb",
                })
            };
    
            function bbb(arg){
                console.log(arg);
            };


        </script>
        
    </body>
</html>
```


### 跨域方法
```
1. 前端把请求发给后端，后端跨域给前端返回数据
2. jsonp
3. nginx设置
4. 响应头添加Access-Control-Allow-Origin
    obj = HttpResopnse("ok")
    obj["Access-Control-Allow-Origin"] = "允许访问的域名，或IP地址"
    obj["Access-Control-Allow-Origin"] = "*"
```
