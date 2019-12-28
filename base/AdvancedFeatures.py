#Slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

r1 = L[0:3]
print(r1)

r1_1 = L[:3]
print(r1_1)

r2 = L[1:3]
print(r2)

#The last element's index is -1
r2_2 = L[-2:]
print(r2_2)

L2 = list(range(1, 100))

#[a:b:c] a:begin, b:end, c:intreval
r3 = L2[::5]
print(r3)

#[:] means copy a list


print('===================================')
#===================================

#Iteration

#Judge a object can iterable?
# from collections import Iterable
# isinstance('abc', Iterable)

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)


#===================================
print('===================================')
#List Comprehensions
#create a list
r4 = [x * x for x in range(1, 10)]
print(r4)

#create a list with condition
r5 = [x * x for x in range(1, 10) if x % 2 == 0]
print(r5)

#create two loops
r6 = [m + n for m in 'ABC' for n in 'XYZ']
print(r6)

#get key and value
d2 = {'x': 'A', 'y': 'B', 'z': 'C'}
r7 = [k + '=' + v for k, v in d2.items()]
print(r7)

#transform the first letter to lower
L3 = ['Hello', 'Wrold', 'IBM', 'Apple']
r8 = [ch.lower() for ch in L3]
print(r8)

#excise
L4 = ['Hello', 'Wrold', 18, 'Apple', None]
result = [s.lower() for s in L4 if isinstance(s, str)]
print(result)

#===================================
print('===================================')

#Generator
#change list's [] to (), then we create a generator
#The generator stroe arithmetic, so we can not get the value
g = (x * x for x in range(10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#change function to generator, the function contain yield key word


#===================================
print('===================================')
#Iterator
#可以被next()函数调用并不断返回下一个值的对象称为迭代器:Iterator
#可以使用isinstance()判断一个对象是否为Iterator对象
from collections import Iterator



isinstance((x for x in range(10)), Iterator)
#True

isinstance([], Iterator)
#False

isinstance({}, Iterator)
#False

isinstance('abc', Iterator)
#False

#生成器都是Iterator对象,但是list,dict,str虽然是Iterable, 却不是Iterator
#如果要把Iterable变成Iterator,可以使用iter()函数

isinstance(iter([]), Iterator)
#True

isinstance(iter({}), Iterator)
#True