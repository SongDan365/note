### xss攻击
```
把用户提交的内容当代码执行
```


### 模版使用
```html
{{ temp | safe }}
```

### 后台使用
```py
from django.utils.safestring import mark_safe
temp = '<a href="http://www.baidu.com">百度</a>'
new_temp = mark_safe(temp)
return render(request, "test.html", {"temp": new_temp})
```
