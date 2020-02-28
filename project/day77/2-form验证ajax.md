### form验证ajax + 显示错误信息
views.py
```py
from django.shortcuts import render,redirect,HttpResponse
from django.forms import Form
from django.forms import fields
from django.forms import widgets

class LoginForm(Form):
    user = fields.CharField(required=True)
    pwd = fields.CharField(min_length=18)


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        obj = LoginForm(request.POST)
        # is_valid()
        """
        1. 获取当前类中所有的字段
        """
        if obj.is_valid():
            print(obj.cleaned_data)
            return redirect('http://www.baidu.com')
        return render(request,'login.html',{'obj': obj})

def ajax_login(request):
    import json
    ret = {'status': True,'msg': None}
    obj = LoginForm(request.POST)
    if obj.is_valid():
        print(obj.cleaned_data)
    else:
        # print(obj.errors) # obj.errors对象
        ret['status'] = False
        ret['msg'] = obj.errors
    v = json.dumps(ret)
    return HttpResponse(v)
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
    <h1>用户登录</h1>
    <form id="f1" action="/login/" method="POST">
        {% csrf_token %}
        <p>
            <input type="text" name="user" />{{ obj.errors.user.0 }}
        </p>
        <p>
            <input type="password" name="pwd" />{{ obj.errors.pwd.0 }}
        </p>
        <input type="submit" value="提交" />
        <a onclick="submitForm();">提交</a>
    </form>
    <script src="/static/jquery-1.12.4.js"></script>
    <script>
        function submitForm(){
            $('.c1').remove();
            $.ajax({
                url: '/ajax_login/',
                type: 'POST',
                data: $('#f1').serialize(),  // 把form里的数据大包成这样user=alex&pwd=456&csrftoen=dfdf\
                dataType:"JSON",
                success:function(arg){
                    console.log(arg);
                    if(arg.status){

                    }else{
                        $.each(arg.msg,function(index,value){
                            console.log(index,value);
                            var tag = document.createElement('span');
                            tag.innerHTML = value[0];
                            tag.className = 'c1';
                            $('#f1').find('input[name="'+ index +'"]').after(tag);
                        })
                    }
                }
            })
        }
    </script>
</body>
</html>
```
