## time模块
```python
import time

time.time()  # timestamp
time.strftime("%Y-%m-%d %X")  # time str '2017-02-15 11:40:53'
time.localtime()  # return time class
time.localtime(1473525444.037215)  # timestamp -> time class
time.gmtime()  # UTC时区的struct_time class
time.gmtime(1473525444.037215)  # timestamp -> time class
time.mktime(time.strftime())  # time clas -> timestamp
time.strftime("%Y-%m-%d %X", time.localtime())  # timestamp -> time str
time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X')  # time str -> timestamp
time.asctime()  # Sun Sep 11 00:43:43 2016
time.ctime()  # Sun Sep 11 00:46:38 2016
time.sleep(3)  # sleep 3 second
```

---

## datetime模块
```python
import datetime, time

datetime.datetime.now()  # 返回 2016-08-19 12:47:03.941925
datetime.date.fromtimestamp(time.time())  # 时间戳直接转成日期格式 2016-08-19
datetime.datetime.now() + datetime.timedelta(3)  # 当前时间+3天
datetime.datetime.now() + datetime.timedelta(-3)  # 当前时间-3天
datetime.datetime.now() + datetime.timedelta(hours=3)  # 当前时间+3小时
datetime.datetime.now() + datetime.timedelta(minutes=30)  # 当前时间+30分

# 时间替换
c_time  = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2))
```

## random模块
```python
import random
 
random.random()  # 大于0且小于1之间的小数
random.randint(1,3)  # return one int 1-3
random.randrange(1,3)  # return one int 1-2
random.choice([1, '23', [4,5]])  # 1或者23或者[4,5]
random.sample([1, '23', [4,5]], 2)  # 列表元素任意2个组合
random.uniform(1, 3)  # 大于1小于3的小数，如1.927109612082716 

# 打乱item的顺序,相当于"洗牌"
item=[1, 3, 5, 7, 9]
random.shuffle(item)
print(item)

# 生成随机验证码
import random

def make_code(n):
    res = ''
    for i in range(n):
        s1 = chr(random.randint(65,90))
        s2 = str(random.randint(0,9))
        res += random.choice([s1,s2])
    return res

print(make_code(9))
```
---

### os模块
```python
# os模块是与操作系统交互的一个接口
os.getcwd()  # 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  # 改变当前脚本工作目录；相当于shell下cd
os.curdir  # 返回当前目录: ('.')
os.pardir  # 获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')  # 可生成多层递归目录
os.removedirs('dirname1')  # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')  # 生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')  # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')  # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  # 删除一个文件
os.rename("oldname", "newname")  # 重命名文件/目录
os.stat('path/filename')  # 获取文件/目录信息
os.sep  # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep  # 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep  # 输出用于分割文件路径的字符串 win下为;,Linux下为:
os.name  # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  # 运行shell命令，直接显示
os.environ  # 获取系统环境变量
os.path.abspath(path)  # 返回path规范化的绝对路径
os.path.split(path)  # 将path分割成目录和文件名二元组返回
os.path.dirname(path)  # 返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)  # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  # 如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  # 如果path是绝对路径，返回True
os.path.isfile(path)  # 如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  # 如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  # 返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  # 返回path所指向的文件或者目录的最后修改时间
os.path.getsize(path)  # 返回path的大小


# 在Linux和Mac平台上，该函数会原样返回path，在windows平台上会将路径中所有字符转换为小写，并将所有斜杠转换为饭斜杠。
>>> os.path.normcase('c:/windows\\system32\\')   
'c:\\windows\\system32\\'   
   

# 规范化路径，如..和/
>>> os.path.normpath('c://windows\\System32\\../Temp/')   
'c:\\windows\\Temp'   

>>> a = '/Users/jieli/test1/\\\a1/\\\\aa.py/../..'
>>> print(os.path.normpath(a))
/Users/jieli/test1
```

路径处理
```python
# 方式一：推荐使用
import os,sys
possible_topdir = os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    os.pardir,  # 上一级
    os.pardir,
    os.pardir
))
sys.path.insert(0,possible_topdir)


# 方式二：不推荐使用
os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

---

### sys module
```python
sys.argv  # 命令行参数List，第一个元素是程序本身路径
sys.exit(n)  # 退出程序，正常退出时exit(0)
sys.version  # 获取Python解释程序的版本信息
sys.maxint  # 最大的Int值
sys.path  # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform  # 返回操作系统平台名称
```

打印进度条
```python
#=========知识储备==========
#进度条的效果
[#             ]
[##            ]
[###           ]
[####          ]

#指定宽度
print('[%-15s]' %'#')
print('[%-15s]' %'##')
print('[%-15s]' %'###')
print('[%-15s]' %'####')

#打印%
print('%s%%' %(100)) #第二个%号代表取消第一个%的特殊意义

#可传参来控制宽度
print('[%%-%ds]' %50) #[%-50s]
print(('[%%-%ds]' %50) %'#')
print(('[%%-%ds]' %50) %'##')
print(('[%%-%ds]' %50) %'###')


#=========实现打印进度条函数==========
import sys
import time

def progress(percent,width=50):
    if percent >= 1:
        percent=1
    show_str=('[%%-%ds]' %width) %(int(width*percent)*'#')
    print('\r%s %d%%' %(show_str,int(100*percent)),file=sys.stdout,flush=True,end='')


#=========应用==========
data_size=1025
recv_size=0
while recv_size < data_size:
    time.sleep(0.1) #模拟数据的传输延迟
    recv_size+=1024 #每次收1024

    percent=recv_size/data_size #接收的比例
    progress(percent,width=70) #进度条的宽度70
```

## shutil模块
```python
# 文件、文件夹、压缩包 处理模块


import shutil

shutil.copyfileobj(open('a.txt', 'r'), open('b.txt', 'w'))  # a文件中的内容覆盖b文件中的内容
shutil.copyfileobj(open('a.txt', 'r'), open('b.txt', 'a'))  # a文件内容追加到b文件中

# 复制文件
shutil.copyfile("a.txt", "b.txt")

# 仅复制文件的权限
shutil.copymode("a.txt", "b.txt")

# 仅复制文件状态信息
shutil.copystat('f1.log', 'f2.log') #目标文件必须存在

# 拷贝文件和权限
shutil.copy('f1.log', 'f2.log')

# 拷贝文件和状态信息
shutil.copy2('f1.log', 'f2.log')

# 递归的去拷贝文件夹
#目标目录不能存在，注意对folder2目录父级目录要有可写权限，ignore的意思是排除
shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))

# 拷贝软连接
# 通常的拷贝都把软连接拷贝成硬链接，即对待软连接来说，创建新的文件
shutil.copytree('f1', 'f2', symlinks=True, ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))

# 递归的去删除文件
shutil.rmtree('folder1')

# 递归的去移动文件，它类似mv命令，其实就是重命名
shutil.move('folder1', 'folder3')

# 打包压缩文件，返回路径
# data_bak是压缩后的文件名，gztar是压缩格式
# format： 压缩包种类，“zip”, “tar”, “bztar”，“gztar”
# root_dir： 要压缩的文件夹路径（默认当前目录）
# owner： 用户，默认当前用户
# group： 组，默认当前组
# logger： 用于记录日志，通常是logging.Logger对象
ret = shutil.make_archive("data_bak", 'gztar', root_dir='/data')


# shutil 对压缩包的处理是调用 ZipFile 和 TarFile 两个模块来进行的。
# zipfile压缩解压缩
import zipfile

# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')
z.write('a.log')
z.write('data.data')
z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall(path='.')
z.close()

# tarfile压缩解压缩
import tarfile

# 压缩
>>> t=tarfile.open('/tmp/egon.tar','w')
>>> t.add('/test1/a.py',arcname='a.bak')
>>> t.add('/test1/b.py',arcname='b.bak')
>>> t.close()


# 解压
>>> t=tarfile.open('/tmp/egon.tar','r')
>>> t.extractall('/egon')
>>> t.close()
```
