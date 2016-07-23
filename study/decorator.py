"""
장식자.
숫자만 받고 인자는 무제한. 인자를 abs절대값 처리해주는 함수.

ex) absolute->
    def mysum1(x,y,z)
        return x+y+z
"""


def absolute(fn):
    def wrap(list):
        for i in list:
            i = abs(i)
        sum = fn(list)
        return sum
    return wrap


@absolute
def mysum(list):
    return sum(list)

print(mysum([-1,2,3]))

def absolute2(fn):
    def wrap(*args):
        mylist=[]
        for arg in args:
            mylist.append(abs(arg))
        result= fn(*mylist)
        return result
    return wrap

@absolute2
def mysum2(*args):
    return sum(args)

print(mysum2(1,2,3,-100))

