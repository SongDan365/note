### orm字段
```py
AutoField(Field)
    - int自增列，必须填入参数 primary_key=True

BigAutoField(AutoField)
    - bigint自增列，必须填入参数 primary_key=True

    注：当model中如果没有自增列，则自动会创建一个列名为id的列
    from django.db import models

    class UserInfo(models.Model):
        # 自动创建一个列名为id的且为自增的整数列
        username = models.CharField(max_length=32)

    class Group(models.Model):
        # 自定义自增列
        nid = models.AutoField(primary_key=True)
        name = models.CharField(max_length=32)

SmallIntegerField(IntegerField):
    - 小整数 -32768 ～ 32767

PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)
    - 正小整数 0 ～ 32767
IntegerField(Field)
    - 整数列(有符号的) -2147483648 ～ 2147483647

PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)
    - 正整数 0 ～ 2147483647

BigIntegerField(IntegerField):
    - 长整型(有符号的) -9223372036854775808 ～ 9223372036854775807

BooleanField(Field)
    - 布尔值类型

NullBooleanField(Field):
    - 可以为空的布尔值

CharField(Field)
    - 字符类型
    - 必须提供max_length参数， max_length表示字符长度

TextField(Field)
    - 文本类型

EmailField(CharField)：
    - 字符串类型，Django Admin以及ModelForm中提供验证机制

IPAddressField(Field)
    - 字符串类型，Django Admin以及ModelForm中提供验证 IPV4 机制

GenericIPAddressField(Field)
    - 字符串类型，Django Admin以及ModelForm中提供验证 Ipv4和Ipv6
    - 参数：
        protocol，用于指定Ipv4或Ipv6， 'both',"ipv4","ipv6"
        unpack_ipv4， 如果指定为True，则输入::ffff:192.0.2.1时候，可解析为192.0.2.1，开启刺功能，需要protocol="both"

URLField(CharField)
    - 字符串类型，Django Admin以及ModelForm中提供验证 URL

SlugField(CharField)
    - 字符串类型，Django Admin以及ModelForm中提供验证支持 字母、数字、下划线、连接符（减号）

CommaSeparatedIntegerField(CharField)
    - 字符串类型，格式必须为逗号分割的数字

UUIDField(Field)
    - 字符串类型，Django Admin以及ModelForm中提供对UUID格式的验证

FilePathField(Field)
    - 字符串，Django Admin以及ModelForm中提供读取文件夹下文件的功能
    - 参数：
            path,                      文件夹路径
            match=None,                正则匹配
            recursive=False,           递归下面的文件夹
            allow_files=True,          允许文件
            allow_folders=False,       允许文件夹

FileField(Field)
    - 字符串，路径保存在数据库，文件上传到指定目录
    - 参数：
        upload_to = ""      上传文件的保存路径
        storage = None      存储组件，默认django.core.files.storage.FileSystemStorage

ImageField(FileField)
    - 字符串，路径保存在数据库，文件上传到指定目录
    - 参数：
        upload_to = ""      上传文件的保存路径
        storage = None      存储组件，默认django.core.files.storage.FileSystemStorage
        width_field=None,   上传图片的高度保存的数据库字段名（字符串）
        height_field=None   上传图片的宽度保存的数据库字段名（字符串）

DateTimeField(DateField)
    - 日期+时间格式 YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]

DateField(DateTimeCheckMixin, Field)
    - 日期格式      YYYY-MM-DD

TimeField(DateTimeCheckMixin, Field)
    - 时间格式      HH:MM[:ss[.uuuuuu]]

DurationField(Field)
    - 长整数，时间间隔，数据库中按照bigint存储，ORM中获取的值为datetime.timedelta类型

FloatField(Field)
    - 浮点型

DecimalField(Field)
    - 10进制小数
    - 参数：
        max_digits，小数总长度
        decimal_places，小数位长度

BinaryField(Field)
    - 二进制类型
```

### 创建admin用户
```bash
python manage.py createsuperuser
```

### admin注册
```py
# admin.py文件
from django.contrib import admin
from app01 import models
admin.site.register(models.UserInfo)  # 注册完就可以使用admin了
```

### 枚举
```py
color_list = (
    (1,'黑色'),
    (2,'白色'),
    (3,'蓝色')
)
color = models.IntegerField(choices=color_list)
```

### 字段参数
```py
null                数据库中字段是否可以为空
db_column           数据库中字段的列名
default             数据库中字段的默认值
primary_key         数据库中字段是否为主键
db_index            数据库中字段是否可以建立索引
unique              数据库中字段是否可以建立唯一索引
unique_for_date     数据库中字段【日期】部分是否可以建立唯一索引
unique_for_month    数据库中字段【月】部分是否可以建立唯一索引
unique_for_year     数据库中字段【年】部分是否可以建立唯一索引

verbose_name        Admin中显示的字段名称
blank               Admin中是否允许用户输入为空
editable            Admin中是否可以编辑
help_text           Admin中该字段的提示信息
choices             Admin中显示选择框的内容，用不变动的数据放在内存中从而避免跨表操作
                    如：gf = models.IntegerField(choices=[(0, '何穗'),(1, '大表姐'),],default=1)

error_messages      自定义错误信息（字典类型），从而定制想要显示的错误信息；
                    字典健：null, blank, invalid, invalid_choice, unique, and unique_for_date
                    如：{'null': "不能为空.", 'invalid': '格式错误'}

validators          自定义错误验证（列表类型），从而定制想要的验证规则
                    from django.core.validators import RegexValidator
                    from django.core.validators import EmailValidator,URLValidator,DecimalValidator,\
                    MaxLengthValidator,MinLengthValidator,MaxValueValidator,MinValueValidator
                    如：
                        test = models.CharField(
                            max_length=32,
                            error_messages={
                                'c1': '优先错信息1',
                                'c2': '优先错信息2',
                                'c3': '优先错信息3',
                            },
                            validators=[
                                RegexValidator(regex='root_\d+', message='错误了', code='c1'),
                                RegexValidator(regex='root_112233\d+', message='又错误了', code='c2'),
                                EmailValidator(message='又错误了', code='c3'), ]
                        )
```
