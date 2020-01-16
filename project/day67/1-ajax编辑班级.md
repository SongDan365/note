### 阻止a标签默认事件的发生
```html
<!--
    1. onclick 的时候用 return
    2. 函数 return false;
-->
<a href="http://www.baidu.com" onclick="return aaa()">点击</a>
<script>
    function aaa(){
        return false;
    }
</script>
```

### jquery取父标签
```html
$(".a").parent();
```

### jquery取上面的兄弟标签
```html
$(".a").prevAll()
```

### js字符串和json对象转换
```js
json_boj = JSON.parse(str)
str = JSON.stringify(json_boj)
```

### js当前页面刷新
```js
location.reload();
```

### ajax编辑班级
urls.py
```py
from django.urls import path
from app01 import views

urlpatterns = [
    path("ajax_edit_class", views.ajax_edit_class),
]
```

views.py
```py
from django.shortcuts import render, redirect, HttpResponse
import pymysql
from utils import sqlhelper

def ajax_edit_class(request):
    result = {"status": True, "msg":""}
    try:
        class_id = request.POST.get("class_id")
        class_title = request.POST.get("class_title")
        sqlhelper.update("update class set title=%s where id=%s", [class_title, class_id])
    except Exception as e:
        result["status"] = False
        result["msg"] = "异常处理"

    import json
    return HttpResponse(json.dumps(result))
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
            <a onclick="show_model()">ajax添加班级</a>
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
                <td><a href="edit_class?id={{ class.id }}">编辑</a> | <a onclick="model_edit(this)">ajax编辑</a> | <a href="del_class/?id={{ class.id }}">删除</a></td>
            </tr>
            {% endfor %}
        </table>
        <div id="shadow" class="hide shadow"> </div>
        <div id="edit_model" class="model hide">
            <h1>编辑班级</h1>
            <form method="post" action="ajax_add_class">
                <input id="class_id" style="display: none" name="id">
                <p><input id="class_title" type="text" name="title"/><span id="error_msg"></span></p>
                <input type="button" value="提交" onclick="edit_send()"/>
                <input type="button" value="取消" onclick="cancle_edit_model();"/>
            </form>
        </div>
        <script src="/static/jquery/jquery.js"></script>
        <script>
            function model_edit(self){
                document.getElementById("edit_model").classList.remove("hide");
                document.getElementById("shadow").classList.remove("hide");
                ele_list = $(self).parent().prevAll();
                var class_id = $(ele_list[1]).text();
                var class_title = $(ele_list[0]).text();
                $("#class_id").val(class_id);
                $("#class_title").val(class_title);
            }

            function cancle_edit_model(){
                document.getElementById("shadow").classList.add("hide");
                document.getElementById("edit_model").classList.add("hide");
            }

            function edit_send(){
                var class_id = $("#class_id").val();
                var class_title = $("#class_title").val();
                $.ajax({
                    url: "ajax_edit_class",
                    type: "post",
                    data: {"class_id": class_id, "class_title": class_title},
                    success: function (arg) {
                        var arg = JSON.parse(arg) 
                        if(arg.status){
                            location.reload();
                        }else{
                            console.log(arg.msg);
                        }
                    }
                })
            }
        </script>
    </body>
</html>
```
