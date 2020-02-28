### 原生ajax
urls.py
```py
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path("index/", views.Index.as_view()),
    path("add1/", views.Add1.as_view()),
]
```

views.py
```py
from django.shortcuts import render, redirect, HttpResponse
from django.views import View

class Index(View):
    def get(self, request):
        return render(request, "index.html")

class Add1(View):
    def post(self, request):
        i1 = request.POST.get("i1")
        i2 = request.POST.get("i2")
        print(i1)
        print(i2)
        return HttpResponse(int(i1) + int(i2))

class Add2(View):
    def post(self, request):
        return HttpResponse("ok")
```

index.html
```py
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>首页</h1>
        <p><input id="i1"/> + <input id="i2"/> = <input id="i3"/></p>
        <input type="button" value="jquery ajax" onclick="add1()"/>
        <input type="button" value="原生ajax" onclick="add2()"/>
        <script src="/static/jquery.js"></script>
        <script>
            function add1(){
                $.ajax({
                    url: "/add1/",
                    type: "post",
                    data: {"i1": $("#i1").val(), "i2": $("#i2").val()},
                    headers: {"X-CSRFToken": "{{ csrf_token }}"},
                    success: function(arg){
                        $("#i3").val(arg);
                    }
                })
            }

            /* 原生ajax */
            function add2(){
                var xhr = new XMLHttpRequest();
                xhr.onreadystatechange = function(){
                    if(xhr.readyState == 4){
                        document.getElementById("i3").value = xhr.responseText;
                    }
                };
                xhr.open("post", "/add1/");
                xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");

                /* 发post请求必须有下面的头，如果没有头数据在request.body里*/
                xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
                var i1 = document.getElementById("i1").value
                var i2 = document.getElementById("i2").value
                xhr.send("i1=" + i1 + "&i2=" + i2);
            }
        </script>
<!--
XmlHttpRequest对象的主要方法:
a. void open(String method,String url,Boolen async)
   用于创建请求
    
   参数：
       method： 请求方式（字符串类型），如：POST、GET、DELETE...
       url：    要请求的地址（字符串类型）
       async：  是否异步（布尔类型）
 
b. void send(String body)
    用于发送请求
 
    参数：
        body： 要发送的数据（字符串类型）
 
c. void setRequestHeader(String header,String value)
    用于设置请求头
 
    参数：
        header： 请求头的key（字符串类型）
        vlaue：  请求头的value（字符串类型）
 
d. String getAllResponseHeaders()
    获取所有响应头
 
    返回值：
        响应头数据（字符串类型）
 
e. String getResponseHeader(String header)
    获取响应头中指定header的值
 
    参数：
        header： 响应头的key（字符串类型）
 
    返回值：
        响应头中指定的header对应的值
 
f. void abort()
 
    终止请求

----------------------------------------------------

XmlHttpRequest对象的主要属性：
a. Number readyState
   状态值（整数）
 
   详细：
      0-未初始化，尚未调用open()方法；
      1-启动，调用了open()方法，未调用send()方法；
      2-发送，已经调用了send()方法，未接收到响应；
      3-接收，已经接收到部分响应数据；
      4-完成，已经接收到全部响应数据；
 
b. Function onreadystatechange
   当readyState的值改变时自动触发执行其对应的函数（回调函数）
 
c. String responseText
   服务器返回的数据（字符串类型）
 
d. XmlDocument responseXML
   服务器返回的数据（Xml对象）
 
e. Number states
   状态码（整数），如：200、404...
 
f. String statesText
   状态文本（字符串），如：OK、NotFound...
-->
    </body>
</html>
```
