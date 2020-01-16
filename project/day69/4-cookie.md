### 什么是cookie
```py
# cookie是保存在浏览器端的键值对
```

### 写入cookie
views.py
```py
def login(request):
    obj = redirect("/index")
    obj.set_cookie("ticket", "aaa")
    obj.set_cookie("ticket", "aaa", max_age=10)  # cookie有效时间10秒
    import datetime
    from datetime import timedelta  # 时间加减
    ct = datetime.datetime.utctime()  # 当前时间
    v = timedelta(seconds=10)
    value = ct + v
    obj.set_cookie("ticket", "aaa", expires=value)  # cookie有效时间10秒
    request.COOKIES.get("ticket")  # 获取所有的cookie
    obj.set_cookie("ticket", "aaa", path="/",  # cookie有效路径
        domain=None,  # 有效域名
        httponly=None,  # 仅http请求可用，js获取不到
        secure=False,  # https使用
    )
    return obj
```

### 签名cookie
```py
def login(request):
    obj = redirect("/index")
    obj.set_signed_cookie("k1", "v1", salt="111")  # 签名cookie
    request.get_signed_cookie("k1", salt="111")  # 获取签名cookie
```
