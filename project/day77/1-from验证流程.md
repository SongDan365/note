### form验证流程
```py
# 内部原理
                    
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        obj = LoginForm(request.POST)
        # is_valid
        """
        1. LoginForm实例化时，
            self.fields={
                'user': 正则表达式
                'pwd': 正则表达式
            }
        2. 循环self.fields
                flag = True
                errors
                cleaned_data
                for k,v in self.fields.items():
                # 1. user,正则表达式
                input_value = request.POST.get(k)
                正则表达式和input_value
                flag = False
                return flag
        """
        if obj.is_valid():
            print(obj.cleaned_data)
        else:
            print(obj.errors)
        return render(request,'login.html')
```
