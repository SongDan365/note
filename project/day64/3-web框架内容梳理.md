### web框架内容梳理
```
1. Http，无状态，短连接

2. 
    浏览器（socket客户端）
    网站（socket服务端）

3. 自己写网站
    a. socket服务端
    b. 根据URL不同返回不同的内容
        路由系统：
            URL -> 函数
    c. 字符串返回给用户
        模板引擎渲染：
            HTML充当模板（特殊字符）
            自己创造任意数据
            字符串替换
4. Web框架：
    框架种类：
        - a,b,c					 --> Tornado
        - [第三方a],b,c          --> wsgiref -> Django 
        - [第三方a],b,[第三方c]  --> flask,
        
    分类：
        - Django框架（Web。。。。。。）
        - 其他
```
