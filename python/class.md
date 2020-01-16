### __str__
```python
class c1:
    def __str__(self):
        return "c1"

l = c1()
print(l)  # 触发__str__
```

## __add__
```python
class c1:
    def __add__(self, x):  # 必须有一个参数
        print("__add__")

l1 = c1()
l1 + 1  # 触发__add__，l1传给self，1传给x
```

## __dict__
```
class c1:
    name = "aaa"
    age = 18

c1.__dict__  # 查看类的命名空间
x = c1()
x.__class__  # x属于哪个类
c1.__bases__  # 继承哪个类
```

## __getattr__
```
当访问object不存在的属性时会调用该方法
```

## __getattribute__
```
访问object所有属性都会触发
```

## __slots__
```python
class Student(object):
    __slots__ = ('name', 'age')  # 类里只能有这两个属性
```

## __doc__
```
c.__doc__  # 查看注释
```

## __del__
```
class c1:
    pass

l1 = c1()
del l1  # 触发__del__
```

## __or__
```
x | y  # 触发
x or y  # 触发
```

## __call__
```
x()  # 触发
```
__getattr__  # x.undefined
__setattr__  # x.name = "aaa"
__delattr__  # del x.name
__getattribute__  # x.name
__getitem__  # x[key], x[1:2], 没有__iter__时的for循环和其他迭代器
