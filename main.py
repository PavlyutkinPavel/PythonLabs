from SerizalizatorDeserializatorLib import SerializersFactory, SerializerType

"""
def tst2(b=10):
    return b + 1


def tst(a):
    return a + a ** 2


tst3 = lambda x: x ** 2


def gen():
    for i in range(10):
        yield i


def tst5():
    def tst6():
        return 18

    return tst6


class t:
    @staticmethod
    def tst5():
        return "tst5"

    @classmethod
    def clsmet(cls):
        return cls._TST5

    def f(self):
        return 1

    _TST5 = 1 - 0


class T(t):
    _X = 11

    A = 10
    B = 11
    C = 14

    @staticmethod
    def tst4():
        return 123 * T._X

    def init(self):
        self.xy = 10

    def inf(self):
        print(self.xy, " ", self._TST5)


def my_decorator(func):
    def cwrapper(*args, **kwargs):
        print("start func")
        func(*args, **kwargs)
        print("end func")

    return cwrapper


def for_dec(a):
    print("Hello world", a)


df = my_decorator(for_dec)


class A:
    a = "A"


class B(A):
    a = "B"


class C(A):
    a = "C"


class D(B, C):
    a = "D"
"""


import math


class A:
    x = 10

    def my_meth(self, a):
        return math.sin(self.x * a)

    def __str__(self):
        return "a"

    def __repr__(self):
        return "a"


class B:
    def __int__(self):
        self._a = 10

    # @property
    # def a(self):
    #     return self._a

    @classmethod
    def meth_cls(cls):
        return "pass lab"


class C(A, B):
    pass


if __name__ == '__main__':

    s = SerializersFactory.create_serializer(SerializerType.JSON)
    C_ser = s.dumps(C)
    C_des = s.loads(C_ser)
    c = C_des()
    c_ser = s.dumps(c)
    c_des = s.loads(c_ser)
    print(c_des)
    print(c_des.x)
    print(c_des.my_meth(12))
    print(c_des.meth_cls())
    # c = C()
    # s.dumps(c)
    # a = s.loads(c)
    """
    with open("data_file.json", "w") as file:
        
    with open("data_file.json", "r") as file:
    """

    # a = s.dumps(C)
    # a = s.loads(C)
    # c = C_des()



    """
    print(a)

    print(T.__dict__)
    print(a.__dict__)

    print(a)
    print(a._X)
    print(a.A)
    print(a.tst4())
    print(a.clsmet())
    print(a.tst5())
    print(a._TST5)
    """

    # x = JsonSerializer.dumps(T.clsmet)
    # print(x)
    # y = JsonSerializer.loads(x)