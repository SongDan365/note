### form验证错误补充
views.py
```py
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from app01 import models

from app01.forms import RegisterForm
class Register(View):
    def get(self, request):
        obj = RegisterForm(request)
        return render(request, "register.html", {"obj": obj})

    def post(self, request):
        obj = RegisterForm(request, request.POST, request.FILES)
        if obj.is_valid():
            return redirect("/")
            pass
        return render(request, "register.html", {"obj": obj})
```

register.html
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="/static/bootstrap/css/bootstrap.min.css"/>
        <style>
            .login{
                width: 450px;
                margin: 0 auto;
                margin-top: 100px;
            }

            .f1{
                position: absolute;
                width:80px;
                height: 80px;
                top:0;
                left: 0;
                opacity: 0;
            }
        </style>
    </head>
    <body>
        <div class="login">
            <h3>注册</h3>
            <!--获取clean函数里的错误-->
            <h3>{{ obj.non_field_errors }}</h3>
            <form class="form-horizontal" action="/register/" method="post" enctype="multipart/form-data">
                {% csrf_token %}
                <div style="position: relative; width: 80px; height: 80px">
                    <img id="previewImg" src="/static/imgs/default.png" width="80px" height="80px">
                    {{ obj.avatar }}
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">用户名</label>
                    <div class="col-sm-9">
                        {{ obj.username }}
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">密码</label>
                    <div class="col-sm-9">
                        {{ obj.password }} {{ obj.password.errors.0 }}
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">确认密码</label>
                    <div class="col-sm-9">
                        {{ obj.password2 }} {{ obj.password2.errors.0 }}
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">验证码</label>
                    <div class="col-sm-4">
                        {{ obj.code }} {{ obj.code.errors.0 }}
                    </div>
                    <div class="col-sm-5">
                        <img src="/check_code/" style="width: 120px; height: 33px;">
                    </div>
                </div>
                <div class="form-group">
                    <div class="col-sm-offset-2 col-sm-10">
                        <input type="submit" class="btn btn-default" value="登陆">
                    </div>
                </div>
            </form>
        </div>
        <script src="/static/jquery.js"></script>
        <script>
            $(function(){
                bindAvatar();
            });

            function bindAvatar(){
                if(window.URL.createObjectURL){
                    bindAvatar2();
                }else if(window.FileReader){
                    bindAvatar3();
                }else{
                    bindAvatar1();
                };
            };

            function bindAvatar1(){
                $("#imgSelect").change(function(){
                    var obj = $(this)[0].files[0];
                    // ajax发送到后台，获取路径
                    // img.src=获取的路径
                });
            };


            function bindAvatar2(){
                // 本地预览
                $("#imgSelect").change(function(){
                    var obj = $(this)[0].files[0];
                    var v = window.URL.createObjectURL(obj);
                    $("#previewImg").attr("src", v);
                    $("#previewImg").load(function(){
                        // 手动释放内存
                        window.URL.revokeObjectURL(v);
                    });
                });
            };


            function bindAvatar3(){
                // 本地预览
                $("#imgSelect").change(function(){
                    var obj = $(this)[0].files[0];
                    var reader = new FileReader();
                    // 自动释放内存
                    reader.readAsDataURL(obj);
                    reader.onload = function(){
                        $("#previewImg").attr("src", this.result);
                    };
                });
            };
        </script>
    </body>
</html>
```

forms.py
```py
from django.forms import Form, fields, widgets
from django.core.exceptions import ValidationError

class RegisterForm(Form):
    username = fields.CharField(
        widget = widgets.TextInput(attrs={"class": "form-control"})
    )
    password = fields.CharField(
        widget = widgets.PasswordInput(attrs={"class": "form-control"})
            )
    password2 = fields.CharField(
        widget = widgets.PasswordInput(attrs={"class": "form-control"})
    )
    avatar = fields.FileField(
        widget = widgets.FileInput(attrs={"id": "imgSelect", "class": "f1"})
    )
    code = fields.CharField(
        widget = widgets.PasswordInput(attrs={"class": "form-control"})
    )

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_password2(self):
        p1 = self.cleaned_data.get("password")
        p2 = self.cleaned_data.get("password2")
        if p1 == p2:
            return p2
        else:
            raise ValidationError("密码不一致")

    def clean_code(self):
        input_code = self.cleaned_data["code"]
        session_code = self.request.session.get("code")
        if input_code.lower() == session_code.lower():
            return input_code
        raise ValidationError("验证码错误")

    def clean(self):
        p1 = self.cleaned_data.get("password")
        p2 = self.cleaned_data.get("password2")
        if p1 == p2:
            return None
        self.add_error("password", ValidationError("密码不一致"))
        self.add_error("password2", ValidationError("密码不一致"))
```
