### orm配置
settings.py
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "db1",
        'USER': "root",
        'PASSWORD': "1",
        'HOST': "127.0.0.1",
        'PORT': "3306",
    }
}
```

__init__.py
```py
import pymysql
pymysql.install_as_MySQLdb()
```

### 报错设置
/Users/dan/Desktop/python学习/.venv/lib/python3.8/site-packages/django/db/backends/mysql/base.py
```py
# 注释掉这两行
# if version < (1, 3, 3):
#     raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__)
```

/Users/dan/Desktop/python学习/.venv/lib/python3.8/site-packages/django/db/backends/mysql/operations.py
```py
# 把 decode 改成 encode
# if query is not None:
#     query = query.decode(errors='replace')
    
if query is not None:
    query = query.encode(errors='replace')
```
