### 多对多 自建第三张表
```py

class Boy(models.Model):
    name = models.CharField(max_length=32)


class Girl(models.Model):
    nick = models.CharField(max_length=32)

class Love(models.Model):
    b = models.ForeignKey('Boy')
    g = models.ForeignKey('Girl')

    class Meta:
        unique_together = [
            ('b','g'),
        ]
```

### 多对多 ManyToMany 生成第三张表
models.py
```py
from django.db import models

class Boy(models.Model):
    name = models.CharField(max_length=32)
    m = models.ManyToManyField('Girl')


class Girl(models.Model):
    nick = models.CharField(max_length=32)
```

views.py
```py
# 操作ManyToMany生成的第三张表
obj = models.Boy.objects.filter(name='方少伟').first()
print(obj.id,obj.name)
obj.m.add(2)  # 向第三张表里添加数据
obj.m.add(2,4)
obj.m.add(*[1,])

obj.m.remove(1)  # 删除第三张表数据
obj.m.remove(2,3)
obj.m.remove(*[4,])

obj.m.set([1,])  # 重置第三张表

q = obj.m.all()  # [Girl对象]
print(q)
obj = models.Boy.objects.filter(name='方少伟').first()
girl_list = obj.m.all()  # 所有和方少伟有关的girl ob

obj = models.Boy.objects.filter(name='方少伟').first()
girl_list = obj.m.all()
girl_list = obj.m.filter(nick='小鱼')  # 二次筛选
print(girl_list)

obj = models.Boy.objects.filter(name='方少伟').first()
obj.m.clear()  # 清空


obj = models.Girl.objects.filter(nick='小鱼').first()
print(obj.id,obj.nick)
v = obj.boy_set.all()  # manytomany 反向关联
print(v)
```

### 多对多 第三张表 + ManyToMany
```py
# models.py 文件

from django.db import models
class Boy(models.Model):
    name = models.CharField(max_length=32)
    # throught指定使用的表，throught_fields使用的列
    m = models.ManyToManyField('Girl',through="Love",through_fields=('b','g',))


class Girl(models.Model):
    nick = models.CharField(max_length=32)
    # m = models.ManyToManyField('Boy')

class Love(models.Model):
    b = models.ForeignKey('Boy')
    g = models.ForeignKey('Girl')

    class Meta:
        unique_together = [
            ('b','g'),
        ]
```

```py
# views.py文件

obj = models.Boy.objects.filter(name='方少伟').first()
obj.m.add(1)  # 不能添加
obj.m.remove(1)  # 不能删除
obj.m.clear()  # 可以
v = obj.m.all()
print(v)
```
