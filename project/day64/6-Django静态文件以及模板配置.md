### 模版配置
setting.py
```python
# 静态文件配置
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# 模版路径配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],  # 配置模版路径
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 主程序
urls.py
```python
from django.urls import path
from django.shortcuts import render

def login(request):
    return render(request, "login.html")
    
urlpatterns = [
    path('login', login)
]
```

login.html
```html
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/static/commons.css"/>
</head>
<body>
    <h1>用户登陆</h1>
    <form>
        <input type="text"/>
    </form>
</body>
</html>
```

commons.css
```css
h1 {
    color: red;
}
```
