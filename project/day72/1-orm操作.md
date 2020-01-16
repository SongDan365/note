### orm操作
```py
models.UserInfo.objects.all().order_by("id")  # 排序
models.UserInfo.objects.all().order_by("-id")  # 从大到小排序
models.UserInfo.objects.all().order_by("-id", "name")  # 先按id排序，id一样按name排序

from django.db.models import Count
v = models.UserInfo.objects.values("ut_id").annotate(xxx=Count("id"))  # 分组
v.query  # 查看生成了什么sql语句
v = models.UserInfo.objects.values("ut_id").annotate(xxx=Count("id")).filter(xxx__gt=2)  # 分组


models.UserInfo.objects.filter(id_gt=1)
models.UserInfo.objects.filter(id_lt=1)
models.UserInfo.objects.filter(id_lte=1)
models.UserInfo.objects.filter(id__in=[1, 3, 4])
models.UserInfo.objects.filter(id__range=[1, 10])  # 1-10 之间
models.UserInfo.objects.filter(name__startwith="aaa")
models.UserInfo.objects.filter(name__endwith="aaa")
models.UserInfo.objects.filter(name__contains="aaa")
models.UserInfo.objects.exclude(id=1)  # 不等于


models.UserInfo.objects.values("nid").distinct()  # 去重，或者用分组去重
models.UserInfo.objects.all().order_by("-nid").reverse()  # 反转，前面必须有order_by才能用
models.UserInfo.objects.all().only("id", "name")
models.UserInfo.objects.all().defer("id", "name")  # 不取id和name
```

### F
```py
# F 做自家一用
from django.db.models import F
models.UserInfo.objects.all().update(age=F("age")+1)
```

### Q
```py
# Q 复杂条件查询
from django.db.models import Q
models.UserInfo.objects.filter(Q(id=1))
models.UserInfo.objects.filter(Q(id=1) | Q(id=2))  # 或者
models.UserInfo.objects.filter(Q(id=1) & Q(id=2))  # and


q1 = Q()
q1.connector = "OR"
q1.children.append(("id", 1))
q1.children.append(("id", 10))
q1.children.append(("id", 9))

q2 = Q()
q2.connector = "OR"
q2.children.append(("c1", 1))
q2.children.append(("c1", 10))
q2.children.append(("c1", 9))

con = Q()
con.add(q1, "AND")
con.add(q2, "AND")

models.UserInfo.objects.filter(con)
```

### extra
```py
models.UserInfo.objects.all().extra(select={"n": "select count(1) from app01_usertype"})
models.UserInfo.objects.all().extra(select={"n": "select count(1) from app01_usertype where id=%s"}, select_params=[1])
models.UserInfo.objects.all().extra(
    select={
        "n": "select count(1) from app01_usertype where id=%s"
        "m": "select count(1) from app01_usertype where id=%s"
    }, 
    select_params=[1, 2]
)

models.UserInfo.objects.all().extra(
    where=["id=1", "name='aaa'"]
)
models.UserInfo.objects.all().extra(
    where=["id=1 or id=2", "name='aaa'"]
)
models.UserInfo.objects.all().extra(
    where=["id=%s or id=%s", "name=%s"],
    params=[1, 2, "aaa"]
)
models.UserInfo.objects.all().extra(
    order_by=["-id", "name"]
)
models.UserInfo.bojects.all().extra(  # select * from app01_userinfo, app01_usertype
    tables=["app01_usertype"]
)
```

### 原生SQL
```py
from django.db import connection, connections
cursor = connection.cursor()
cursor = connections["default"].cursor()
cursor.execute("select * from app01_userinfo where id=%s", [1])
data = cursor.fetchone()
```

### 
```py
def dates(self, field_name, kind, order='ASC'):
    # 根据时间进行某一部分进行去重查找并截取指定内容
    # kind只能是："year"（年）, "month"（年-月）, "day"（年-月-日）
    # order只能是："ASC"  "DESC"
    # 并获取转换后的时间
        - year : 年-01-01
        - month: 年-月-01
        - day  : 年-月-日

    models.DatePlus.objects.dates('ctime','day','DESC')

def datetimes(self, field_name, kind, order='ASC', tzinfo=None):
    # 根据时间进行某一部分进行去重查找并截取指定内容，将时间转换为指定时区时间
    # kind只能是 "year", "month", "day", "hour", "minute", "second"
    # order只能是："ASC"  "DESC"
    # tzinfo时区对象
    models.DDD.objects.datetimes('ctime','hour',tzinfo=pytz.UTC)
    models.DDD.objects.datetimes('ctime','hour',tzinfo=pytz.timezone('Asia/Shanghai'))

    """
    pip3 install pytz
    import pytz
    pytz.all_timezones
    pytz.timezone(‘Asia/Shanghai’)
    """

def none(self):
    # 空QuerySet对象

def aggregate(self, *args, **kwargs):
   # 聚合函数，获取字典类型聚合结果
   from django.db.models import Count, Avg, Max, Min, Sum
   result = models.UserInfo.objects.aggregate(k=Count('u_id', distinct=True), n=Count('nid'))
   ===> {'k': 3, 'n': 4}

def count(self):
   # 获取个数

def get(self, *args, **kwargs):
   # 获取单个对象

def create(self, **kwargs):
   # 创建对象

def bulk_create(self, objs, batch_size=None):
    # 批量插入
    # batch_size表示一次插入的个数
    objs = [
        models.UserInfo(name='r11'),
        models.UserInfo(name='r22')
    ]
    models.DDD.objects.bulk_create(objs, 10)  # 一次最多提交10个对象

def get_or_create(self, defaults=None, **kwargs):
    # 如果存在，则获取，否则，创建
    # defaults 指定创建时，其他字段的值
    obj, created = models.UserInfo.objects.get_or_create(username='root1', defaults={'email': '1111111','u_id': 2, 't_id': 2})

def update_or_create(self, defaults=None, **kwargs):
    # 如果存在，则更新，否则，创建
    # defaults 指定创建时或更新时的其他字段
    obj, created = models.UserInfo.objects.update_or_create(username='root1', defaults={'email': '1111111','u_id': 2, 't_id': 1})

def first(self):
   # 获取第一个

def last(self):
   # 获取最后一个

def in_bulk(self, id_list=None):
   # 根据主键ID进行查找
   id_list = [11,21,31]
   models.DDD.objects.in_bulk(id_list)

def delete(self):
   # 删除

def update(self, **kwargs):
    # 更新

def exists(self):
   # 是否有结果

def raw(self, raw_query, params=None, translations=None, using=None):
    # 执行原生SQL
    models.UserInfo.objects.raw('select * from userinfo')

    # 如果SQL是其他表时，必须将名字设置为当前UserInfo对象的主键列名
    models.UserInfo.objects.raw('select id as nid from 其他表')

    # 为原生SQL设置参数
    models.UserInfo.objects.raw('select id as nid from userinfo where nid>%s', params=[12,])

    # 将获取的到列名转换为指定列名
    name_map = {'first': 'first_name', 'last': 'last_name', 'bd': 'birth_date', 'pk': 'id'}
    Person.objects.raw('SELECT * FROM some_other_table', translations=name_map)

    # 指定数据库
    models.UserInfo.objects.raw('select * from userinfo', using="default")

    ################### 原生SQL ###################
    from django.db import connection, connections
    cursor = connection.cursor()  # cursor = connections['default'].cursor()
    cursor.execute("""SELECT * from auth_user where id = %s""", [1])
    row = cursor.fetchone() # fetchall()/fetchmany(..)
```
