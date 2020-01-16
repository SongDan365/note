### ajax添加班级 and 模态对话框
urls.py
```py
from django.urls import path
from app01 import views

urlpatterns = [
    path("ajax_add_class", views.ajax_add_class),
]
```

views.py
```py
from django.shortcuts import render, redirect, HttpResponse
from utils import sqlhelper

def ajax_add_class(request):
    title = request.POST.get("title")
    if len(title) > 0:
        sqlhelper.update("insert into class(title) values(%s)", [title])
        return HttpResponse("ok")
    else:
        return HttpResponse("title must be gt 1")
```

class.html
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8"/>
        <style>
            .hide {
                display: none;
            }
            .shadow{
                position: fixed;
                left: 0;
                top: 0;
                right: 0;
                bottom: 0;
                background-color: black;
                opacity: 0.4;
                z-index: 1;
            }
            .model{
                position: fixed;
                z-index: 2;
                left: 50%;
                top: 50%;
                height: 300px;
                width: 400px;
                background-color: white;
                margin-left: -200px;
                margin-top: -150px;
            }
        </style>
    </head>
    <body>
        <h1>班级列表</h1>
        <div>
            <a href="/add_class.html">添加班级</a>
            <a onclick="show_model();">ajax添加班级</a>
        </div>
        <table>
            <tr>
                <th>ID</th>
                <th>title</th>
                <th>操作</th>
            </tr>
            {% for class in class_list %}
            <tr>
                <td>{{ class.id }}</td>
                <td>{{ class.title }}</td>
                <td><a href="edit_class?id={{ class.id }}">编辑</a> | <a href="del_class/?id={{ class.id }}">删除</a></td>
            </tr>
            {% endfor %}
        </table>
        <div id="shadow" class="hide shadow"> </div>
        <div id="model" class="model hide">
            <form method="post" action="ajax_add_class">
                <p><input id="title" type="text" name="title"/><span id="error_msg"></span></p>
                <input type="button" value="提交" onclick="ajax_send();"/>
                <input type="button" value="取消" onclick="cancle_model();"/>
            </form>
        </div>
        <script src="/static/jquery/jquery.js"></script>
        <script>
            function show_model(){
                document.getElementById("shadow").classList.remove("hide");
                document.getElementById("model").classList.remove("hide");
            }

            function cancle_model(){
                document.getElementById("shadow").classList.add("hide");
                document.getElementById("model").classList.add("hide");
            }

            function ajax_send(){
                $.ajax({
                    url: "ajax_add_class",
                    type: "post",
                    data: {"title": $("#title").val()},
                    success: function(data){
                        if(data == "ok"){
                            location.href="/class";
                        }else{
                            $("#error_msg").text(data);
                        }
                    }
                })
            }
        </script>
    </body>
</html>
```
