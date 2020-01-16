### 响应式
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8"/>
        <style>
            .pg-header{
                background-color: black;
                height: 50px;
            }
            <!-- 当宽度小于700px触发 -->
            @media (max-width: 700px) {
                .pg-header{
                    background-color: yellow;
                    height: 50px;
                }
            }
        </style>
    </head>
    <body>
        <div class="pg-header"></div>
    </body>
</html>
```
