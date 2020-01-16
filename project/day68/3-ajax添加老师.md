### ajax添加老师
urls.py
```py
from django.urls import path
from app01 import views

urlpatterns = [
    path("get_class_list", views.get_class_list),
    path("ajax_add_teacher", views.ajax_add_teacher),
]
```

views.py
```py
from django.shortcuts import render, redirect, HttpResponse
import pymysql
from utils import sqlhelper
from utils.sqlhelper import Sqlhelper
import json

def get_class_list(request):
    sql = Sqlhelper()
    class_list = sql.getall("select id, title from class")
    return HttpResponse(json.dumps(class_list))

def ajax_add_teacher(request):
    result = {"status": True, "msg": ""}
    try:
        tname = request.POST.get("tname")
        class_id_list = request.POST.getlist("class_id_list")
        print(class_id_list)
        sql = Sqlhelper()
        teacher_id = sql.update("insert into teacher (name) value (%s)", [tname])
        data_list = [(teacher_id, class_id) for class_id in class_id_list]
        sql.addall("insert into teacher_to_class (teacher_id, class_id) values(%s, %s)", data_list)
        sql.close()
    except Exception as e:
        result["status"] = False
        result["msg"] = e
    return HttpResponse(json.dumps(result))
```

teacher.html
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
            .loading{ <!-- 添加加载页面 -->
                position: fixed;
                width: 300px;
                height: 300px;
                left: 50%;
                top: 50%;
                margin-left: -150px;
                margin-top: -150px;
                background-image: url("/static/loading.gif");
                z-index: 3;
            }
        </style>
    </head>
    <body>
        <h1>老师列表</h1>
        <div>
            <a href="/add_teacher">添加老师</a> | <a id="add_a">ajax添加老师</a>
        </div>
        <table>
            <tr>
                <th>老师ID</th>
                <th>老师名字</th>
                <th>任教班级</th>
                <th>操作</th>
            </tr>
            {% for teacher in teacher_list %}
            <tr>
                <td>{{ teacher.id }}</td>
                <td>{{ teacher.name }}</td>
                <td>
                    {% for title in teacher.titles %}
                    <span>{{ title }}</span>
                    {% endfor %}
                </td>
                <td><a href="/edit_teacher?id={{ teacher.id }}">编辑</a></td>
            </tr>
            {% endfor %}
        </table>
        <div id="shadow" class="shadow hide"> </div>
        <div id="edit_model" class="model hide ">
            <input id="teacher_name" type="text" name="teacher_name"/>
            <select name="class_id_list" multiple size="10"></select>
            <input type="submit"/>
        </div>
        <div class="loading hide"></div>
        <script src="/static/jquery/jquery.js"></script>
        <script>
            $("#add_a").click(function(){
                $("#shadow, .loading").removeClass("hide")  // 同时找到两个标签
                $.ajax({
                    url: "/get_class_list",
                    type: "get",
                    dataType: "json",
                    success: function(args){
                        $.each(args, function(i, row){
                            var tag = document.createElement("option");
                            tag.innerHTML = row.title;
                            tag.setAttribute("value", row.id);
                            $("select").append(tag);
                        })
                        $(".loading").addClass("hide");
                        $("#edit_model").removeClass("hide");
                    }
                })
            })
        </script>
    </body>
</html>
```
