### wsgi
```py
wsgi是一个协议。
socket都遵守这个协议。

django默认用的是wsgiref，wsgiref 性能低，测试用可以。
生产使用uwsgi + django



Wsgi+Django
    from wsgiref.simple_server import make_server
        
        
    def RunServer(environ, start_response):

        Django框架开始
        中间件
        路由系统
        视图函数
        。。。。。
        
        start_response('200 OK', [('Content-Type', 'text/html')])
        
        
        return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]
        
        
    if __name__ == '__main__':
        httpd = make_server('127.0.0.1', 8000, RunServer)
        httpd.serve_forever()
```
