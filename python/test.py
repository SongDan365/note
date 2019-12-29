from functools import wraps

def deco(func):
    @wraps(func) #加在最内层函数正上方,解决函数明的问题
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

@deco
def index():
    '''哈哈哈哈'''
    print('from index')

print(index.__doc__)
print(index)
