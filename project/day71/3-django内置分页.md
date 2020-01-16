### django内置分页
urls.py
```py
from django.urls import re_path
from app01 import views

urlpatterns = [
    re_path("index.html", views.Index.as_view()),
    re_path("index/(\d+).html", views.Index.as_view()),
]
```

views.py
```py
from django.shortcuts import render, HttpResponse
from app01 import models
from django.views import View

class Index(View):

    def get(self, request, *args, **kwargs):
        from django.core.paginator import Paginator, Page

        group_list = models.UserGroup.objects.all()
        if args:
            current_page = args[0]
            paginator = Paginator(group_list, 10)
                # paginator.per_page    每页显示条目数量
                # Paginator.count    数据总个数
                # Paginator.num_pages    总页数
                # Paginator.page_range    总页数的索引范围(1, 10), (1, 200)
                # Paginator.page    page 对象

            posts = paginator.page(current_page)
                # has_next              是否有下一页
                # next_page_number      下一页页码
                # has_previous          是否有上一页
                # previous_page_number  上一页页码
                # object_list           分页之后的数据列表
                # number                当前页
                # paginator             paginator对象
            page_list = [ i for i in posts.paginator.page_range ]
            print(page_list)

            if len(page_list) - int(current_page) > 5:
                page_list = page_list[:int(current_page)+5]
            print(page_list)

            if int(current_page) > 5:
                page_list = page_list[int(current_page)-5:]
            print(page_list)

            return render(request, "index.html", {"group_list": posts.object_list, "posts": posts, "page_list": page_list})
        return render(request, "index.html", {"group_list": group_list})
```

index.html
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <ul>
            {% for group in group_list %}
                <li>{{ group.id }} {{ group.title }}</li>
            {% endfor %}
        </ul>
        <div>
            {% if posts.has_previous %}
            <a href="/index/{{ posts.previous_page_number}}.html">上一页</a>
            {% endif %}
            {% for page in page_list %}
            <a href="/index/{{ page }}.html">{{ page }}</a>
            {% endfor %}
            {% if posts.has_next %}
            <a href="/index/{{ posts.next_page_number}}.html">下一页</a>
            {% endif %}

        </div>
    </body>
</html>
```
