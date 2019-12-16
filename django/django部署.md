## 测试环境启动django
1.修改setting.py文件
```py
ALLOWED_HOSTS = ["本机IP"]
ALLOWED_HOSTS = ["*"]
```

2.运行服务器
```bash
python manage.py runserver 0.0.0.0:8000
```

## 生产环境运行django
1.安装uwsgi
```bash
pip3 install uwsgi
```

2.修改settings.py文件
```python
# 在配置文件最后添加下面内容
# STATIC_ROOT 不能和 STATICFILES_DIRS同时存在
STATIC_ROOT = os.path.join(BASE_DIR, 'static_dir')
```

2.收集静态文件
```bash
python3 manage.py collectstatic static_dir
```

3.修改settings.py文件
```python
# 注释掉这一行，收集完静态文件就可以注释掉了
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_dir')
```

4.写一个uwsgi的配置文件 /project_dir/uwsgi_settings.ini
```ini
[uwsgi]
socket = 127.0.0.1:8000
chdir = /project_dir
wsgi_file = /project_dir/project_dir/wsgi.py
processes = 4
threads = 2
```

5.运行uwsgi程序
```bash
uwsgi uwsgi_settings.ini
```

6.配置nginx
```nginx.conf
upstream django {
    server 127.0.0.1:8000;
}
server {
    listen 80;
    location /static {
        alias /static_dir;
    }
    location / {
        uwsgi_pass django;
        include uwsgi_params;
    }
}
```

6.启动nginx
```bash
service nginx start
```
