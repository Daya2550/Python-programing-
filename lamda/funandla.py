def add(n):
    return lambda a : a+n
print(add(5)(5))

def sub(n1):
    return lambda n2 : n1-n2
a=sub(5)

print(a(5))