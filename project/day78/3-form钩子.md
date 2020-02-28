### form钩子
views.py
```py
from django.core.exceptions import ValidationError

class TestForm(Form):
    # 执行顺序user -> clean_user -> pwd -> clean_pwd
    user = fields.CharField()
    pwd = fields.CharField()

    # 钩子函数
    def clean_user(self):
        v = self.cleaned_data["user"]
        if models.Student.objects.filter(name=v).count():
            raise ValidationError("用户名已经存在", code="invalid")
        return self.cleaned_data["user"]

    def clean_pwd(self):
        pass

    def clean(self):
        # 所有的字段都执行完，执行这个函数
        pass

    def _post_clean(self):
        # 在clean后面执行，和clean一样，clean有异常处理，这个方法没有异常处理，必须自己写异常处理
        pass
```
