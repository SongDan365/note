### orm创建表
settings.py
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "app01",  # 添加这行，注册app
]
```

models.py
```py
from django.db import models

class UserGroup(models.Model):
    title = models.charField(max_length=32)

class UserInfo(models.Model):
    # nid = models.AutoField()  # int 不写自动创建
    # nid = models.BigAutoField(primary_key=True)  # big int
    username = models.CharField(max_length=32)  # char类型
    password = models.CharField(max_length=64)
    ug = models.ForeignKey("UserGroup", null=True)  # 外键
```

执行命令
```bash
# 创建表和修改表都是执行这个两个命令
python manage.py makemigrations
python manage.py migrate
```
