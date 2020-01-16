### ajax编辑学生
urls.py
```py
from django.urls import path
from app01 import views

urlpatterns = [
    path("ajax_edit_student", views.ajax_edit_student),
]
```

views.py
```py
from django.shortcuts import render, redirect, HttpResponse
import pymysql
from utils import sqlhelper
import json

def ajax_edit_student(request):
    result = {"status": True, "msg": ""}
    try:
        student_id = request.POST.get("student_id")
        student_name = request.POST.get("student_name")
        class_id = request.POST.get("class_id")
        sqlhelper.update("update student set name=%s, class_id=%s where id=%s", [student_name, class_id, student_id])
    except Exception as e:
        result["status"] = False
        result["msg"] = e
    return HttpResponse(json.dumps(result))
```

student.html
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
        <h1>学生列表</h1>
        <div>
            <a href="/add_student.html">添加学生</a>
            <a id="ajax_add_student">添加学生</a>
        </div>
        <table>
            <tr>
                <th>学生ID</th>
                <th>学生姓名</th>
                <th>班级ID</th>
                <th>所属班级</th>
                <th>操作</th>
            </tr>
            {% for student in student_list %}
            <tr>
                <td>{{ student.id }}</td>
                <td>{{ student.name }}</td>
                <td>{{ student.class_id }}</td>
                <td>{{ student.title }}</td>
                <td><a href="edit_student?id={{ student.id }}">编辑</a> | <a class="show_edit_model">ajax编辑</a> | <a href="del_student/?id={{ student.id }}">删除</a></td>
            </tr>
            {% endfor %}
        </table>
        <div id="shadow" class="hide shadow"> </div>
        <div id="add_student_model" class="model hide">
            <h1>添加学生</h1>
            <p><input id="student_name" type="text" name="name"/></p>
            <select id="class_id" name="class_id">
                {% for class in class_list %}
                <option value="{{ class.id }}">{{ class.title }}</option>
                {% endfor %}
            </select>
            <input id="send_student" type="button" value="提交"/>
            <input id="cancle_add" type="button" value="取消"/>
        </div>
        <div id="edit_box" class="model hide">
            <h1>编辑学生</h1>
            <p><input id="edit_id" type="text" name="id"/></p>
            <p><input id="edit_name" type="text" name="name"/></p>
            <select id="edit_class_id" name="class_id">
                {% for class in class_list %}
                <option value="{{ class.id }}">{{ class.title }}</option>
                {% endfor %}
            </select>
            <input id="edit_submit" type="button" value="提交"/>
            <input id="edit_cancle" type="button" value="取消"/>
        </div>
        <script src="/static/jquery/jquery.js"></script>
        <script>
            $("#ajax_add_student").click(function(){
                $("#shadow").removeClass("hide");
                $("#add_student_model").removeClass("hide");
            })

            $("#cancle_add").click(function(){
                $("#shadow").addClass("hide");
                $("#add_student_model").addClass("hide");
            })

            $("#send_student").click(function(){
                var student_name = $("#student_name").val();
                var class_id = $("#class_id").val();
                $.ajax({
                    url: "ajax_add_student",
                    type: "post",
                    data: {"student_name": student_name, "class_id": class_id},
                    success: function(arg){
                        var arg = JSON.parse(arg);
                        if(arg.status){
                            location.reload();
                        }else{
                            console.log(arg.msg);
                        }
                    }
                })
            });

            $(".show_edit_model").click(function(){
                var tds = $(this).parent().prevAll();
                var student_id = $(tds[3]).text();
                var student_name = $(tds[2]).text();
                var class_id = $(tds[1]).text();
                $("#edit_id").val(student_id);
                $("#edit_name").val(student_name);
                $("#edit_class_id").val(class_id);
                $("#shadow").removeClass("hide");
                $("#edit_box").removeClass("hide");
            });

            $("#edit_cancle").click(function(){
                $("#shadow").addClass("hide");
                $("#edit_box").addClass("hide");
            });

            $("#edit_submit").click(function(){
                $.ajax({
                    url: "ajax_edit_student",
                    type: "post",
                    data: {"student_id": $("#edit_id").val(), "student_name": $("#edit_name").val(), "class_id": $("#edit_class_id").val()},
                    dataType: "json",  // 等与JSON.parse(arg)
                    success: function(arg){
                        if(arg.status){
                            location.reload();
                        }else{
                            console.log(arg.msg);
                        }
                    }
                })
            })
        </script>
    </body>
</html>
```
