### csrf
```
跨站脚本攻击
```

views.py
```py
from django.views.decorators.csrf import csrf_exempt,csrf_protect  #csrf_exempt局部禁用，csrf_protect局部使用

@eascsrf_protect
def csrf1(request):

    if request.method == 'GET':
        return render(request,'csrf1.html')
    else:
        return HttpResponse('ok')

from django.views import View
from django.utils.decorators import method_decorator

# 1. CBV应用装饰器
def wrapper(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner
# 1. 指定方法上添加装饰器

    # class Foo(View):
    #
    #     @method_decorator(wrapper)
    #     def get(self,request):
    #         pass
    #
    #     def post(self,request):
    #         pass
# 2. 在类上添加
#     @method_decorator(wrapper,name='dispatch')
#     class Foo(View):
#
#         def get(self,request):
#             pass
#
#         def post(self,request):
#             pass
```

csrf1.html
```py
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <form method="POST" action="/csrf1.html">
        {% csrf_token %} <!-- 写了这个csrf就能通过，cookie里也有 -->
        <input type="text" name="user" />
        <input type="submit" value="提交"/>
    </form>
</body>
</html>
```

setting.py
```py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # 注释后整个网站都不用csrf验证。
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### csrf ajax提交
```py
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <form method="POST" action="/csrf1.html">
        {% csrf_token %}
        <input id="user" type="text" name="user" />
        <input type="submit" value="提交"/>
        <a onclick="submitForm();">Ajax提交</a>
    </form>
    <script src="/static/jquery-1.12.4.js"></script>
    <script src="/static/jquery.cookie.js"></script>

    <script>
        // 方法1
        function submitForm(){
            var token = $("input[name='csrfmiddlewaretoken']").val();
            var user = $('#user').val();
            $.ajax({
                url: '/csrf1.html',
                type: 'POST',
                data: { "user":user, "csrfmiddlewaretoken": csrf},
                success:function(arg){
                    console.log(arg);
                }
            })
        }


        // 方法2，需要jquery.cookie.js
        function submitForm(){
            var token = $.cookie('csrftoken');
            var user = $('#user').val();
            $.ajax({
                url: '/csrf1.html',
                type: 'POST',
                headers:{'X-CSRFToken': token},  // 添加请求头
                data: { "user":user},
                success:function(arg){
                    console.log(arg);
                }
            })
        }
    </script>
</body>
</html>
```
