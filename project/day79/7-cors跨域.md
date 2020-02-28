### CORS跨域
```
随着技术的发展，现在的浏览器可以支持主动设置从而允许跨域请求，即：跨域资源共享（CORS，Cross-Origin Resource Sharing），其本质是设置响应头，使得浏览器允许跨域请求。
```

### 简单请求 OR 非简单请求
```
条件：
    1、请求方式：HEAD、GET、POST
    2、请求头信息：
        Accept
        Accept-Language
        Content-Language
        Last-Event-ID
        Content-Type 对应的值是以下三个中的任意一个
                                application/x-www-form-urlencoded
                                multipart/form-data
                                text/plain
 
注意：同时满足以上两个条件时，则是简单请求，否则为复杂请求
```

### 简单请求和非简单请求的区别？
```
简单请求：一次请求
非简单请求：两次请求，在发送数据之前会先发一次请求用于做“预检”，只有“预检”通过后才再发送一次请求用于数据传输。
```

### 关于“预检”
```
- 请求方式：OPTIONS
- “预检”其实做检查，检查如果通过则允许传输数据，检查不通过则不再发送真正想要发送的消息
- 如何“预检”
     => 如果复杂请求是PUT等请求，则服务端需要设置允许某请求，否则“预检”不通过
        Access-Control-Request-Method
     => 如果复杂请求设置了请求头，则服务端需要设置允许某请求头，否则“预检”不通过
        Access-Control-Request-Headers
```

```
a、支持跨域，简单请求

服务器设置响应头：Access-Control-Allow-Origin = '域名' 或 '*'



b、支持跨域，复杂请求
预检请求是OPTIONS请求
由于复杂请求时，首先会发送“预检”请求，如果“预检”成功，则发送真实数据。

“预检”请求时，允许请求方式则需服务器设置响应头：Access-Control-Allow-Methods = "DELETE"
“预检”请求时，允许请求头则需服务器设置响应头：Access-Control-Request-Headers
“预检”缓存时间，服务器设置响应头：Access-Control-Max-Age


c、跨域获取响应头
默认获取到的所有响应头只有基本信息，如果想要获取自定义的响应头，则需要再服务器端设置Access-Control-Expose-Headers。


d、跨域传输cookie

在跨域请求中，默认情况下，HTTP Authentication信息，Cookie头以及用户的SSL证书无论在预检请求中或是在实际请求都是不会被发送。

如果想要发送：

浏览器端：XMLHttpRequest的withCredentials为true
服务器端：Access-Control-Allow-Credentials为true
注意：服务器端响应的 Access-Control-Allow-Origin 不能是通配符 *
```
