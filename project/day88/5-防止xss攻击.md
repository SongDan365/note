### 防止xss攻击
forms.py
```py
class ArticleForm(Form):

    title = fields.CharField(max_length=64)

    content = fields.CharField(
        widget=widgets.Textarea(attrs={'id':'i1'})
    )

    def clean_content(self):
        old = self.cleaned_data['content']
        from utils.xss import xss

        return xss(old)

        # from bs4 import BeautifulSoup
        #
        # valid_tag = {
        #     'p': ['class','id'],
        #     'img':['src'],
        #     'div': ['class']
        # }
        #
        # old = self.cleaned_data['content']
        # soup = BeautifulSoup(old,'html.parser')
        #
        # tags = soup.find_all()
        # for tag in tags:
        #     if tag.name not in valid_tag:
        #         tag.decompose()
        #     if tag.attrs:
        #         for k in list(tag.attrs.keys()): # {id:'i1',a=123,b=999}
        #             if k not in valid_tag[tag.name]:
        #                 del tag.attrs[k]
        # content_str = soup.decode()
```

views.py
```py
CONTENT = ""
from app01.forms import ArticleForm
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
        KindEditor.create("#i1",{
            width: "700px",
            height: "300px",
            resizeType:1,
            uploadJson: '/upload_img.html',
            extraFileUploadParams:{
                "csrfmiddlewaretoken":"{{ csrf_token }}"
            }
        })
    </script>

</body>
</html>
```

xss.py
```py
from bs4 import BeautifulSoup

def xss(old):
    valid_tag = {
        'p': ['class','id'],
        'img':['src'],
        'div': ['class']
    }

    soup = BeautifulSoup(old,'html.parser')

    tags = soup.find_all()
    for tag in tags:
        if tag.name not in valid_tag:
            tag.decompose()
        if tag.attrs:
            for k in list(tag.attrs.keys()): # {id:'i1',a=123,b=999}
                if k not in valid_tag[tag.name]:
                    del tag.attrs[k]
    content_str = soup.decode()
    return content_str
```
