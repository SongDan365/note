### js实现多级评论
article.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <style>
        .comment{
            margin-left: 30px;
        }
    </style>
</head>
<body>
    <div class="c1">
        <div class="c11">{{ blog.user.nickname }}</div>
        <div class="c12">{{ blog.title }}</div>
    </div>
    <div class="c2">
        <h3>分类</h3>
        <ul>
            {% for item in category_list %}
                <li>
                    <a href="/{{ blog.site }}/category/{{ item.category_id }}/">{{ item.category__title }}({{ item.ct }})</a>
                </li>
            {% endfor %}
        </ul>
    </div>
    <div class="c3">
        <h3>标签</h3>
        <ul>
            {% for item in tag_list %}
                <li>
                    <a href="/{{ blog.site }}/tag/{{ item.tag_id }}/">{{ item.tag__title }}({{ item.ct }})</a>
                </li>
            {% endfor %}
        </ul>
    </div>
    <div>
        <h3>时间</h3>
        <ul>
            {% for item in date_list %}
                <li>
                    <a href="/{{ blog.site }}/date/{{ item.ctime }}/">{{ item.ctime }}({{ item.ct }})</a>
                </li>
            {% endfor %}
        </ul>
    </div>

    <div>
        <h3><a>{{ obj.title }}</a></h3>
        {{ obj.articledetail.content|safe }}
    </div>
    <a onclick="updown(this,{{ obj.nid }},1);">
        <span>赞</span>
        <i>{{ obj.up_count }}</i>
    </a>
    <a onclick="updown(this,{{ obj.nid }},0);">
        <span>踩</span>
        <i>{{ obj.down_count }}</i>
    </a>
    <h3>评论</h3>
    <div id="commentArea">

    </div>
{#    {{ comment_str|safe }}#}
    <script src="/static/jquery-1.12.4.js"></script>
    <script>
        /*
        1. 调用对象方法时，通过调用类的prototype中的方法，可以扩展
        2. 正则表达式 /\w+/g
        3. 字符串replace
                ''.replace('alex','sb');
                ''.replace(/\w+/,'sb');
                ''.replace(/\w+/g,'sb');
                ''.replace(/(\w+)/g,function(k,kk){return 11;});
        */
        String.prototype.Format = function(arg){
            /*
            this,当前字符串  "i am {name1}, age is {age9}"
             arg,Format方法传入的参数 {name:'alex',age:18}
             return，格式化之后获取的新内容 i am alex, age is 18
            */
            var temp = this.replace(/\{(\w+)\}/g,function(k,kk){
                return arg[kk];
            });
            return temp;
        };

        $(function(){
            // 发送Ajax请求，获取所有评论信息
            // 列表
            // js生成结构
            $.ajax({
                url: '/comments-{{ obj.nid }}.html',
                type:'GET',
                dataType:"JSON",
                success:function(arg){
                    if(arg.status){
                        /*
                         * [ {},{},{}]
                          *
                          * */
                        var comment = commentTree(arg.data);
                        $('#commentArea').append(comment);
                    }else{
                        alert(arg.msg);
                    }
                }
            })

        });

        function commentTree(commentList){
            var comment_str = "<div class='comment'>";
            $.each(commentList,function(k,row){
                // var temp = "<div class='content'>"+ row.content +"</div>";
                var temp = "<div class='content'>{content}</div>".Format({content:row.content});
                comment_str += temp;
                if(row.child.length>0){
                    comment_str += commentTree(row.child);
                }

            });
            comment_str += '</div>';

            return comment_str;
        }

        function updown(ths,nid,val){
            $.ajax({
                url: '/up.html',
                data:{'val':val,'nid':nid,'csrfmiddlewaretoken':'{{ csrf_token }}'},
                type: "POST",
                dataType:'JSON',
                success:function(arg){
                    if(arg.status){
                        // 显示赞个数+1
                    }else{
                        // 显示错误信息
                    }
                }
            })
        }

        function up(ths,nid){
            $.ajax({
                url: '/up.html',
                data:{'val':1,'nid':nid,'csrfmiddlewaretoken':'{{ csrf_token }}'},
                type: "POST",
                dataType:'JSON',
                success:function(arg){
                    if(arg.status){
                        // 显示赞个数+1
                    }else{
                        // 显示错误信息
                    }
                }
            })
        }

        function down(ths,nid){
            $.ajax({
                url: '/up.html',
                data:{'val':0,'nid':nid,'csrfmiddlewaretoken':'{{ csrf_token }}'},
                type: "POST",
                dataType:'JSON',
                success:function(arg){
                    if(arg.status){
                        // 显示踩个数+1
                    }else{
                        // 显示错误信息
                    }
                }
            })
        }
    </script>
</body>
</html>
```

views.py
```py
def comments(request,nid):
    response = {'status':True,'data':None,'msg':None}
    try:
        msg_list = [
            {'id':1,'content':'写的太好了','parent_id':None},
            {'id':2,'content':'你说得对','parent_id':None},
            {'id':3,'content':'顶楼上','parent_id':None},
            {'id':4,'content':'你眼瞎吗','parent_id':1},
            {'id':5,'content':'我看是','parent_id':4},
            {'id':6,'content':'鸡毛','parent_id':2},
            {'id':7,'content':'你是没呀','parent_id':5},
            {'id':8,'content':'惺惺惜惺惺想寻','parent_id':3},
        ]
        msg_list_dict = {}
        for item in msg_list:
            item['child'] = []
            msg_list_dict[item['id']] = item
        result = []
        for item in msg_list:
            pid = item['parent_id']
            if pid:
                msg_list_dict[pid]['child'].append(item)
            else:
                result.append(item)
        response['data'] = result
    except Exception as e:
        response['status'] = False
        response['msg'] = str(e)

    return HttpResponse(json.dumps(response))
```
