class c1:
    def __add__(self, x):  # 必须有一个参数
        print("__add__")

l1 = c1()
l1 + 1  # 触发__add__
