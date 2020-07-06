def decorate(func):
    def inner(a,b):
        ret = func(a,b)
        return abs(ret)
    return inner

def sub(a,b):
    return a - b

print(sub(3,4))
sub = decorate(sub)
print(sub(3,4))