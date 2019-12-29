# 1.先设计接口函数
# 2.B类按照接口区写代码
# 3.C类按照接口去调用代码
# 这样B类的方法改动不会影响到其他调用者的使用
from abc import abstractmethod, ABCMeta

class A(metaclass=ABCMeta):
    @abstractmethod
    def test(self, x):
        pass


class B(A):
    def test(self, x)
        print(x)


class C:
    def foo(self, obj):
        obj.test(123)
