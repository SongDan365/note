### kindEditor使用
urls.py
```py
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^wangzhe.html$', views.wangzhe),
]
```

views.py
```py
def wangzhe(request):
    if request.method == "GET":
        obj = ArticleForm()
        return render(request,'wangzhe.html',{'obj':obj})
    else:
        obj = ArticleForm(request.POST)
        if obj.is_valid():
            content = obj.cleaned_data['content']
            global CONTENT
            CONTENT = content
            print(content)
            return HttpResponse('...')


def upload_img(request):
    import os
    upload_type = request.GET.get('dir')
    file_obj = request.FILES.get('imgFile')
    file_path = os.path.join('static/imgs',file_obj.name)
    with open(file_path,'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)

    dic = {
        'error': 0,
        'url': '/' + file_path,
        'message': '错误了...'
    }
    import json
    return HttpResponse(json.dumps(dic))
```

wangzhe.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <form method="POST" action="/wangzhe.html" novalidate>
        {% csrf_token %}
        <p>
            文章标题
            {{ obj.title }}
        </p>

        <div>
            <div>文章内容</div>
            <div>
                {{ obj.content }}
            </div>
        </div>
        <input type="submit" value="提交" />
    </form>
    <script src="/static/kindeditor-4.1.10/kindeditor-all.js"></script>
    <script>
        // 应用kindeditor
        KindEditor.create("#i1",{
            width: "700px",
            height: "300px",
            resizeType:1,
            // 上传图片
            uploadJson: '/upload_img.html',
            extraFileUploadParams:{
                "csrfmiddlewaretoken":"{{ csrf_token }}"
            }
        })
    </script>

</body>
</html>
```





###########################################################################
### 前端编辑器插件
```
前端插件：CKEditor,TinyEditor,UEEditor,KindEditor
kindeditor官网 www.kindeditor.net
```

### kindeditor
```
2. 下载
    官网下载：http://kindeditor.net/down.php
    本地下载：http://files.cnblogs.com/files/wupeiqi/kindeditor_a5.zip

3. 文件夹说明
    ├── asp                          asp示例
    ├── asp.net                    asp.net示例
    ├── attached                  空文件夹，放置关联文件attached
    ├── examples                 HTML示例
    ├── jsp                          java示例
    ├── kindeditor-all-min.js 全部JS（压缩）
    ├── kindeditor-all.js        全部JS（未压缩）
    ├── kindeditor-min.js      仅KindEditor JS（压缩）
    ├── kindeditor.js            仅KindEditor JS（未压缩）
    ├── lang                        支持语言
    ├── license.txt               License
    ├── php                        PHP示例
    ├── plugins                    KindEditor内部使用的插件
    └── themes                   KindEditor主题

4.基本使用
    <textarea name="content" id="content"></textarea>
    
    <script src="/static/jquery-1.12.4.js"></script>
    <script src="/static/plugins/kind-editor/kindeditor-all.js"></script>
    <script>
        $(function () {
            initKindEditor();
        });
    
        function initKindEditor() {
            var kind = KindEditor.create('#content', {
                width: '100%',       // 文本框宽度(可以百分比或像素)
                height: '300px',     // 文本框高度(只能像素)
                minWidth: 200,       // 最小宽度（数字）
                minHeight: 400      // 最小高度（数字）
            });
        }
    </script>

5.详细参数
    http://kindeditor.net/docs/option.html
```


### 文件上传示例
```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>

<div>
    <h1>文章内容</h1>
    {{ request.POST.content|safe }}
</div>


<form method="POST">
    <h1>请输入内容：</h1>
    {% csrf_token %}
    <div style="width: 500px; margin: 0 auto;">
        <textarea name="content" id="content"></textarea>
    </div>
    <input type="submit" value="提交"/>
</form>

<script src="/static/jquery-1.12.4.js"></script>
<script src="/static/plugins/kind-editor/kindeditor-all.js"></script>
<script>
    $(function () {
        initKindEditor();
    });

    function initKindEditor() {
        var a = 'kind';
        var kind = KindEditor.create('#content', {
            width: '100%',       // 文本框宽度(可以百分比或像素)
            height: '300px',     // 文本框高度(只能像素)
            minWidth: 200,       // 最小宽度（数字）
            minHeight: 400,      // 最小高度（数字）
            uploadJson: '/kind/upload_img/',
            extraFileUploadParams: {
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            fileManagerJson: '/kind/file_manager/',
            allowPreviewEmoticons: true,
            allowImageUpload: true
        });
    }
</script>
</body>
</html>
```

views.py
```py
import os
import json
import time

from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    """
    首页
    :param request:
    :return:
    """
    return render(request, 'index.html')


def upload_img(request):
    """
    文件上传
    :param request:
    :return:
    """
    dic = {
        'error': 0,
        'url': '/static/imgs/20130809170025.png',
        'message': '错误了...'
    }

    return HttpResponse(json.dumps(dic))


def file_manager(request):
    """
    文件管理
    :param request:
    :return:
    """
    dic = {}
    root_path = '/Users/wupeiqi/PycharmProjects/editors/static/'
    static_root_path = '/static/'
    request_path = request.GET.get('path')
    if request_path:
        abs_current_dir_path = os.path.join(root_path, request_path)
        move_up_dir_path = os.path.dirname(request_path.rstrip('/'))
        dic['moveup_dir_path'] = move_up_dir_path + '/' if move_up_dir_path else move_up_dir_path

    else:
        abs_current_dir_path = root_path
        dic['moveup_dir_path'] = ''

    dic['current_dir_path'] = request_path
    dic['current_url'] = os.path.join(static_root_path, request_path)

    file_list = []
    for item in os.listdir(abs_current_dir_path):
        abs_item_path = os.path.join(abs_current_dir_path, item)
        a, exts = os.path.splitext(item)
        is_dir = os.path.isdir(abs_item_path)
        if is_dir:
            temp = {
                'is_dir': True,
                'has_file': True,
                'filesize': 0,
                'dir_path': '',
                'is_photo': False,
                'filetype': '',
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }
        else:
            temp = {
                'is_dir': False,
                'has_file': False,
                'filesize': os.stat(abs_item_path).st_size,
                'dir_path': '',
                'is_photo': True if exts.lower() in ['.jpg', '.png', '.jpeg'] else False,
                'filetype': exts.lower().strip('.'),
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }

        file_list.append(temp)
    dic['file_list'] = file_list
    return HttpResponse(json.dumps(dic))
```

### 7、XSS过滤特殊标签
```
处理依赖
    pip3 install beautifulsoup4
```

```py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup


class XSSFilter(object):
    __instance = None

    def __init__(self):
        # XSS白名单
        self.valid_tags = {
            "font": ['color', 'size', 'face', 'style'],
            'b': [],
            'div': [],
            "span": [],
            "table": [
                'border', 'cellspacing', 'cellpadding'
            ],
            'th': [
                'colspan', 'rowspan'
            ],
            'td': [
                'colspan', 'rowspan'
            ],
            "a": ['href', 'target', 'name'],
            "img": ['src', 'alt', 'title'],
            'p': [
                'align'
            ],
            "pre": ['class'],
            "hr": ['class'],
            'strong': []
        }

    @classmethod
    def instance(cls):
        if not cls.__instance:
            obj = cls()
            cls.__instance = obj
        return cls.__instance

    def process(self, content):
        soup = BeautifulSoup(content, 'lxml')
        # 遍历所有HTML标签
        for tag in soup.find_all(recursive=True):
            # 判断标签名是否在白名单中
            if tag.name not in self.valid_tags:
                tag.hidden = True
                if tag.name not in ['html', 'body']:
                    tag.hidden = True
                    tag.clear()
                continue
            # 当前标签的所有属性白名单
            attr_rules = self.valid_tags[tag.name]
            keys = list(tag.attrs.keys())
            for key in keys:
                if key not in attr_rules:
                    del tag[key]

        return soup.renderContents()


if __name__ == '__main__':
    html = """<p class="title">
                        <b>The Dormouse's story</b>
                    </p>
                    <p class="story">
                        <div name='root'>
                            Once upon a time there were three little sisters; and their names were
                            <a href="http://example.com/elsie" class="sister c1" style='color:red;background-color:green;' id="link1"><!-- Elsie --></a>
                            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                            <a href="http://example.com/tillie" class="sister" id="link3">Tilffffffffffffflie</a>;
                            and they lived at the bottom of a well.
                            <script>alert(123)</script>
                        </div>
                    </p>
                    <p class="story">...</p>"""

    v = XSSFilter.instance().process(html)
    print(v)
```

基于__new__实现单例模式示例
```py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup


class XSSFilter(object):
    __instance = None

    def __init__(self):
        # XSS白名单
        self.valid_tags = {
            "font": ['color', 'size', 'face', 'style'],
            'b': [],
            'div': [],
            "span": [],
            "table": [
                'border', 'cellspacing', 'cellpadding'
            ],
            'th': [
                'colspan', 'rowspan'
            ],
            'td': [
                'colspan', 'rowspan'
            ],
            "a": ['href', 'target', 'name'],
            "img": ['src', 'alt', 'title'],
            'p': [
                'align'
            ],
            "pre": ['class'],
            "hr": ['class'],
            'strong': []
        }

    def __new__(cls, *args, **kwargs):
        """
        单例模式
        :param cls:
        :param args:
        :param kwargs:
        :return:
        """
        if not cls.__instance:
            obj = object.__new__(cls, *args, **kwargs)
            cls.__instance = obj
        return cls.__instance

    def process(self, content):
        soup = BeautifulSoup(content, 'lxml')
        # 遍历所有HTML标签
        for tag in soup.find_all(recursive=True):
            # 判断标签名是否在白名单中
            if tag.name not in self.valid_tags:
                tag.hidden = True
                if tag.name not in ['html', 'body']:
                    tag.hidden = True
                    tag.clear()
                continue
            # 当前标签的所有属性白名单
            attr_rules = self.valid_tags[tag.name]
            keys = list(tag.attrs.keys())
            for key in keys:
                if key not in attr_rules:
                    del tag[key]

        return soup.renderContents()


if __name__ == '__main__':
    html = """<p class="title">
                        <b>The Dormouse's story</b>
                    </p>
                    <p class="story">
                        <div name='root'>
                            Once upon a time there were three little sisters; and their names were
                            <a href="http://example.com/elsie" class="sister c1" style='color:red;background-color:green;' id="link1"><!-- Elsie --></a>
                            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                            <a href="http://example.com/tillie" class="sister" id="link3">Tilffffffffffffflie</a>;
                            and they lived at the bottom of a well.
                            <script>alert(123)</script>
                        </div>
                    </p>
                    <p class="story">...</p>"""

    obj = XSSFilter()
    v = obj.process(html)
    print(v)
```
