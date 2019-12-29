#Higher-order function
#funcname is also a variable
f = abs
print(f(-20))

#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, -6, abs))

print('-------------------------')
#map/reduce
#map:
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

#reduce:
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))


#map() and reduce() we will see you later

print('=============================filter==================================')


#filter

#删除偶数,保留奇数
def is_odd(n):
    return n % 2 == 1

r1 = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(r1)

#删除空字符串
def not_empty(s):
    return s and s.strip()

r2 = list(filter(not_empty, ['A', '', 'B', None, 'C', ' ']))
print(r2)

print('===============================================================')

#sorted

print('===============================================================')


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)

    return fs

f1, f2, f3 = count()

print(f1(), f2(), f3())

print('==============================lambda=================================')

#lambda (Anonymous function)
#lambda x: x * x
def f(x):
    return x * x

fc = lambda n: n % 2 == 1

L = list(filter(fc, range(1, 20)))
# L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)


print('=============================Decorator==================================')
#Decorator
#在代码运行期间动态增加功能的方式,称之为'装饰器'

def now():
    print('2015-3-25')

f = now
print(f())

print(now.__name__)
print(f.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper()

@log
def now():
    print('2015-3-25')


print('=============================Partial function==================================')
#Partical function
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
#fuctools.partial就是帮助我们创建一个偏函数的,不需要我们自己定义int2(),可以直接使用上面的代码创建一个新的函数int2
#当函数的参数个数太多,需要简化时,使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。