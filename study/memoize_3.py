
def base(base_i):
    def wrap(fn):
        def inner(x,y):
            return base_i+ abs(fn(x,y))
        return inner
    return wrap

def verbose(fn):
    def wrap(*args):
        print("함수호출 : {}".format(args))
        return fn(*args)
    return wrap


def alert(maximum):
    def wrap(fn):
        def inner(x,y):
            result = x + y
            if result > maximum:
                print("삐삐삐!!")
            return result
        return inner
    return wrap

@alert(10)
def mysum1(x,y):
    return x +y

@base(10)
def mysum2(x,y):
    return x + y

print(mysum1(9,2))
print(mysum2(2,1))
