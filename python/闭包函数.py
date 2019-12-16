# 闭包定义
# 内部函数包含对外部函数作用域的引用而非全局作用域的引用

def external_function():
    a = 1

    def intrinsic_function():
        nonlocal a    # 声明a是上一级函数的变量，如果上一级函数没有这个变量会报错
        b = a
        return b
    return intrinsic_function

f = external_function()
print(f())
print(f.__closure__[0].cell_contents)  # 查看闭包函数的元素
