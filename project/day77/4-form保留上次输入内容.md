### from保留上次输入内容
views.py
```py
from django.shortcuts import render
from django.views import View
from django.forms import Form, fields

# Create your views here.
class TestForm(Form):
    t1 = fields.CharField(required=True, max_length=8, min_length=2,
        error_messages={
            "required": "不能为空",
            "max_length": "太长",
            "min_length": "太短"
        }
    )
    t2 = fields.IntegerField()

class Test(View):
    def get(self, request):
        obj = TestForm()
        return render(request, "test.html", {"obj": obj})

    def post(self, request):
        obj = TestForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
        print(obj.errors)
        return render(request, "test.html", {"obj": obj})
```

test.html
```py
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <form action="/test/" method="post" novalidate>
            {% csrf_token %}
            <p>
                {{ obj.t1 }} {{ obj.errors.t1.0 }}
            </p>
            <p>
                {{ obj.t2 }} {{ obj.errors.t2.0 }}
            </p>
            <input type="submit" value="提交"/>
        </form>
    </body>
</html>
```
