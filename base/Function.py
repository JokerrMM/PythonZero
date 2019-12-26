#defin function
def testFun():
    pass

#Multiple parameters
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]

print(calc(1, 2))

print(calc(*nums))

#*args是可变参数， args接收的是一个tuple
#**kw是关键字参数，kw接收的是一个dict

#Keywords parameter
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw)

print(person('Michael', 30))

print(person('Bob', 35, city='Beijing'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))

#Named keywords
def personOne(name, age, **kw):
    if 'city' in kw:
        #have 'city' parameter
        pass #do nothing
    if 'job' in kw:
        #have 'job' parameter
        pass
    print('name:', name, 'age:', age, 'other:', kw)


#Recursive function
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)
    pass