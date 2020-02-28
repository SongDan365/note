### session
```py
# 存在服务器端的键值对
```

### 使用session
```py
from django.shortcuts import render,HttpResponse,redirect
from app01 import models
def test(request):

    response = HttpResponse("aaa")
    response.set_cookie('k3','v3')  # 设置cookie
    request.COOKIES.get("k3")  # 获取cookie
    return response


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.UserAdmin.objects.filter(username=u,password=p).first()
        if obj:
            # 1. 生成随机字符串
            # 2. 通过cookie发送给客户端
            # 3. 服务端保存
            # {
            #   随机字符串1: {'username':'alex','email':x''...}
            # }
            request.session['username'] = obj.username  # 把数据放到session里，session 存在django_session表里
            return redirect('/index/')
        else:
            return render(request,'login.html',{'msg':'用户名或密码错误'})


def index(request):
    # 1. 获取客户端端cookie中的随机字符串
    # 2. 去session中查找有没有随机字符
    # 3. 去session对应key的value中查看是否有 username
    v = request.session.get('username')  # 获取session里的值
    if v:
        return HttpResponse('登录成功:%s' %v)
    else:
        return redirect('/login/')


```

### session
```py
# Django中默认支持Session，其内部提供了5种类型的Session供开发者使用：
# 
# 数据库（默认）
# 缓存
# 文件
# 缓存+数据库
# 加密cookie
```

### 数据库session
```py
Django默认支持Session，并且默认是将Session数据存储在数据库中，即：django_session 表中。
 
a. 配置 settings.py
 
    SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）
     
    SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
    SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
    SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
    SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
    SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
    SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
    SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
    SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
 
 
 
b. 使用
 
    def index(request):
        # 获取、设置、删除Session中数据
        request.session['k1']
        request.session.get('k1',None)
        request.session['k1'] = 123
        request.session.setdefault('k1',123) # 存在则不设置
        del request.session['k1']
 
        # 所有 键、值、键值对
        request.session.keys()
        request.session.values()
        request.session.items()
        request.session.iterkeys()
        request.session.itervalues()
        request.session.iteritems()
 
 
        # 用户session的随机字符串
        request.session.session_key
 
        # 将所有Session失效日期小于当前日期的数据删除
        request.session.clear_expired()
 
        # 检查 用户session的随机字符串 在数据库中是否
        request.session.exists("session_key")
 
        # 删除当前用户的所有Session数据
        request.session.delete("session_key")
 
        request.session.set_expiry(value)
            * 如果value是个整数，session会在些秒数后失效。
            * 如果value是个datatime或timedelta，session就会在这个时间后失效。
            * 如果value是0,用户关闭浏览器session就会失效。
            * 如果value是None,session会依赖全局session失效策略。
```

### 缓存Session
```py
a. 配置 settings.py
 
    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
    SESSION_CACHE_ALIAS = 'default'                            # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
 
 
    SESSION_COOKIE_NAME ＝ "sessionid"                        # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
    SESSION_COOKIE_PATH ＝ "/"                                # Session的cookie保存的路径
    SESSION_COOKIE_DOMAIN = None                              # Session的cookie保存的域名
    SESSION_COOKIE_SECURE = False                             # 是否Https传输cookie
    SESSION_COOKIE_HTTPONLY = True                            # 是否Session的cookie只支持http传输
    SESSION_COOKIE_AGE = 1209600                              # Session的cookie失效日期（2周）
    SESSION_EXPIRE_AT_BROWSER_CLOSE = False                   # 是否关闭浏览器使得Session过期
    SESSION_SAVE_EVERY_REQUEST = False                        # 是否每次请求都保存Session，默认修改之后才保存
 
 
 
b. 使用
 
    同上
```

### 文件Session
```
a. 配置 settings.py
 
    SESSION_ENGINE = 'django.contrib.sessions.backends.file'    # 引擎
    SESSION_FILE_PATH = None                                    # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()                                                            # 如：/var/folders/d3/j9tj0gz93dg06bmwxmhh6_xm0000gn/T
 
 
    SESSION_COOKIE_NAME ＝ "sessionid"                          # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
    SESSION_COOKIE_PATH ＝ "/"                                  # Session的cookie保存的路径
    SESSION_COOKIE_DOMAIN = None                                # Session的cookie保存的域名
    SESSION_COOKIE_SECURE = False                               # 是否Https传输cookie
    SESSION_COOKIE_HTTPONLY = True                              # 是否Session的cookie只支持http传输
    SESSION_COOKIE_AGE = 1209600                                # Session的cookie失效日期（2周）
    SESSION_EXPIRE_AT_BROWSER_CLOSE = False                     # 是否关闭浏览器使得Session过期
    SESSION_SAVE_EVERY_REQUEST = False                          # 是否每次请求都保存Session，默认修改之后才保存
 
b. 使用
 
    同上
```

### 缓存+数据库Session
```
数据库用于做持久化，缓存用于提高效率
 
a. 配置 settings.py
 
    SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'        # 引擎
 
b. 使用
 
    同上
```

### 加密cookie Session
```
a. 配置 settings.py
     
    SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'   # 引擎
 
b. 使用
 
    同上
```

### Session用户验证
```
def login(func):
    def wrap(request, *args, **kwargs):
        # 如果未登陆，跳转到指定页面
        if request.path == '/test/':
            return redirect('http://www.baidu.com')
        return func(request, *args, **kwargs)
    return wrap
```
