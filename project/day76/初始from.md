### 初始form
views.py
```py
from django.shortcuts import render,HttpResponse,redirect
from django.forms import Form
from django.forms import fields

class LoginForm(Form):
    # username 和前端提交的名字必须一样
    username = fields.CharField(
        max_length=18,
        min_length=6,
        required=True,  # 不能为空
        error_messages={
            'required': '用户名不能为空',
            'min_length': '太短了',
            'max_length': '太长了',
        }
    )
    # 正则验证: 不能为空，16+
    password = fields.CharField(min_length=16,required=True)
    # email = fields.EmailField()
    # email = fields.GenericIPAddressField()
    # email = fields.IntegerField()


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
       obj = LoginForm(request.POST)
       if obj.is_valid():  # 验证用户提交的数据格式是否正确
           print(obj.cleaned_data) # 字典类型，验证成功后的到的数据
           return redirect('http://www.baidu.com')
       else:
           # 用户输入格式错误
           # obj.errors 所有的错误信息
           return render(request,'login.html',{'obj':obj})
```

login.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <form method="POST" action="/login/">
        {% csrf_token %}
        <p>
            用户：<input type="text" name="username"/>{{ obj.errors.username.0 }}
        </p>
        <p>
            密码：<input type="password" name="password"/>{{ obj.errors.password.0 }}
        </p>
        <input type="submit" value="提交" />{{ msg }}
    </form>
</body>
</html>
```
