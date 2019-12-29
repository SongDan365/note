## 变量的定义
```
name = 'Sam'
sex = 'male'
age = 18
level = 10
```

## 变量的定义规范
```
1. 变量名只能是 字母、数字或下划线的任意组合
2. 变量名的第一个字符不能是数字
3. 关键字不能声明为变量名[
   'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 
   'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

## 定义方式
```
驼峰体
    NumberOfStudents = 80

下划线(推荐使用)
    number_of_students = 80
```

## 定义变量名不好的方式
```
1. 变量名为中文、拼音
2. 变量名过长
3. 变量名词不达意
```

## 变量的id, type, value
```
==比较的是value，
is比较的是id

强调：
    id相同，意味着type和value必定相同
    value相同type肯定相同，但id可能不同,如下

>>> x = "Age: 18"
>>> y = "Age: 18"
>>> id(x)
4424536624
>>> id(y)
4424536688
>>> x == y
True
>>> x is y
False
```

##  常量
```
常量即指不变的量，如pai 3.141592653..., 或在程序运行过程中不会改变的量

常量定义用全大写表示
TELEPHONE = 123456789
```

## 用户与程序交互
```
用户输入任何值，都存成字符串类型
>>> n = input("Number: ")
Number: 123
>>> n
'123'
>>> type(n)
<class 'str'>
```

## 注释
```
单行注释用 #
多行注释用 """ """
```

## 头文件
```
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
```

## 数字
```
int整型
在32位机器上，整数的位数为32位，取值范围为-2**31～2**31-1，即-2147483648～2147483647
在64位系统上，整数的位数为64位，取值范围为-2**63～2**63-1，即-9223372036854775808～9223372036854775807
定义：age = 10  # age = int(10)

float浮点型
定义：salary = 3.1  # salary = float(3.1)

complex复数型
>>> x=1-2j
>>> x.imag
-2.0
>>> x.real
1.0
```

## 字符串
```
在python中，加了引号的字符就是字符串类型，python并没有字符类型。
定义：name = 'aaa'  # name = str('aaa')
```

## 单引号，双引号，三引号的区别
```
单双引号木有任何区别，只有下面这种情况 你需要考虑单双的配合
msg = "My name is Sam , I'm 18 years old!"

多引号什么作用呢？作用就是多行字符串必须用多引号
msg = '''
今天我想写首小诗，
歌颂我的同桌，
你看他那乌黑的短发，
好像一只炸毛鸡。
'''
print(msg)
```

## 字符串拼接
```
字符串能进行"相加"和"相乘"运算。
>>> name = 'Sam'
>>> age = '18'
>>> name + age  # 相加其实就是简单拼接
'Sam18'
>>> name * 5
'SamSamSamSamSam'


注意1：字符串相加的效率不高
字符串1 + 字符串2，并不会在字符串1的基础上加字符串2，而是申请一个全新的内存空间存入字符串1和字符串2，相当字符串1与字符串2的空间被复制了一次，

注意2：只能字符串加字符串，不能字符串加其他类型
```

## 列表
```
在[]内用逗号分隔，可以存放n个任意类型的值
定义：students = ['aaa', 'bbb', 'ccc']  # students = list(['aaa', 'bbb', 'ccc']) 
用于标识：存储多个值的情况，比如一个人有多个爱好
```

## 列表嵌套、取值
```
存放多个学生的信息：姓名，年龄，爱好
>>> students_info = [['aaa', 18, ['play']], ['bbb', 18, ['play', 'sleep']]]
>>> students_info[0][2][0]  # 取出第一个学生的第一个爱好
'play'
```

## 字典
```
在{}内用逗号分隔，可以存放多个key:value的值，value可以是任意类型
定义：info={'name':'Sam', 'age':18, 'sex':18}  # info=dict({'name':'Sam','age':18,'sex':18})
用于标识：存储多个值的情况，每个值都有唯一一个对应的key，可以更为方便高效地取值
```

## 字典相关的嵌套、取值
```
info={
    'name':'egon',
    'hobbies':['play','sleep'],
    'company_info':{
        'name':'Oldboy',
        'type':'education',
        'emp_num':40,
    }
}
print(info['company_info']['name']) #取公司名


students=[
    {'name':'alex','age':38,'hobbies':['play','sleep']},
    {'name':'egon','age':18,'hobbies':['read','sleep']},
    {'name':'wupeiqi','age':58,'hobbies':['music','read','sleep']},
]
print(students[1]['hobbies'][1]) #取第二个学生的第二个爱好
```

## 布尔
```
布尔值，一个True一个False
计算机俗称电脑，即我们编写程序让计算机运行时，应该是让计算机无限接近人脑，或者说人脑能干什么，计算机就应该能干什么，人脑的主要作用是数据运行与逻辑运算，此处的布尔类型就模拟人的逻辑运行，
即判断一个条件成立时，用True标识，不成立则用False标识
>>> a=3
>>> b=5
>>> a > b #不成立就是False,即假
False
>>> a < b #成立就是True, 即真
True

接下来就可以根据条件结果来干不同的事情了：
if a > b 
   print(a is bigger than b )
else 
   print(a is smaller than b )
上面是伪代码，但意味着， 计算机已经可以像人脑一样根据判断结果不同，来执行不同的动作。


布尔类型的重点知识！！！：
    所有数据类型都自带布尔值
    1、None，0，空（空字符串，空列表，空字典等）三种情况下布尔值为False
    2、其余均为真
```

## 可变类型和不可变类型
```
#1.可变类型：在id不变的情况下，value可以变，则称为可变类型，如列表，字典

#2. 不可变类型：value一旦改变，id也改变，则称为不可变类型（id变，意味着创建了新的内存空间）
```

## 格式化输出
```
#%s字符串占位符：可以接收字符串，也可接收数字
print('My name is %s,my age is %s' %('egon',18))

#%d数字占位符：只能接收数字
print('My name is %s,my age is %d' %('egon',18))
print('My name is %s,my age is %d' %('egon','18')) #报错

#接收用户输入，打印成指定格式
name=input('your name: ')
age=input('your age: ') #用户输入18,会存成字符串18,无法传给%d

print('My name is %s,my age is %s' %(name,age))

#注意：
#print('My name is %s,my age is %d' %(name,age)) #age为字符串类型,无法传给%d,所以会报错
```

## 算数运算
```
>>> a = 10
>>> b = 20

>>> a + b
30
>>> a -b 
-10
>>> a * b
200
>>> b / a
2
>>> b % a  # 取余
0
>>> a ** b  # 10的20次方
10000000000000000000
>>> a // b  # 整除
```

## 比较运算
```
>>> a = 10
>>> b = 20
>>> a == b
False
>>> a != b
Ture
>>> a <> b
Ture
>>> a > b
False
>>> a < b
True
>>> a >= b
False
>>> a <= b
Ture
```

## 赋值运算
```
>>> a = 10
>>> a += 10  # a = a + 10
>>> a -= 10  # a = a - 10
a *= 10  # a = a * 10
a /= 10  # a = a / 10
a %= 10  # a = a % 10
a **= 10  # a = a ** 10
a //= 10  # a = a // 10
```

## 逻辑运算
```
and
    Ture and True -> Ture
    False and False -> False
    Ture and False -> False
or
    >>> True or True
    True
    >>> False or False
    False
    >>> True or False
    True
not
    >>> not True
    False
    >>> not False
    True

#三者的优先级从高到低分别是：not，or，and
#最好使用括号来区别优先级，其实意义与上面的一样
```

## 流程控制之if...else
```
if 条件1:
    ...
elif 条件2:
    ...
else:
    ...
```

## 流程控制之while循环
```
count=0
while count <= 10:
    print('loop',count)
    count+=1

死循环
while True:
    pass

break 跳出整个循环
continue 跳出本次循环
while 循环正常执行完，中间没有被break 中止的话，就会执行else后面的语句
```

## 流程控制之for循环
```
for i in range(10):
    pass

break, continue, else 同上
```










