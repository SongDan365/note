### 创建python虚拟环境
```bash
python3.8 -m venv dir_name  # 创建虚拟环境
source dir_name/bin/activate  # 运行虚拟环境
```

### 在虚拟环境安装扩展包
```bash
source dir_name/bin/activate  # 运行虚拟环境
pip install package_name  # 安装包
pip install --upgrade package_name  # 升级包
pip uninstall package_name  # 卸载包
pip show package_name  # 显示包信息
pip list # 显示所有已经安装的包
```

### 安装Django
```bash
pip3 install django
```

### 创建Django项目
```bash
django-admin startproject mysite

# 进入程序目录
cd mysite

# 启动socket服务端，等待用户发送请求
python manage.py runserver 127.0.0.1:8080

# 对当前Django程序所有操作都可以基于manage.py操作
```
