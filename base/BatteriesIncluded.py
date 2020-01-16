print('=============================datetime==================================')
# 获取当前日期和时间
from datetime import datetime
now = datetime.now()
print(now)

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20) #用指定日期时间创建datetime
print(dt)

# datetime转换为timestamp
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00

print('=============================collections==================================')
# 集合模块,提供了许多有用的集合类

from collections import namedtuple
# namedtuple 可以很方便的定义一种数据类型, 它具备了tuple的不变性, 又可以根据属性来引用
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

Circle = namedtuple('Circle', ['x', 'y', 'r'])


#deque
#deque是为了高效实现插入和删除操作的双向列表, 适合用于队列和栈
#deque支持append(), appendleft(), pop(), popleft()
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

#defaultdict
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

from collections import defaultdict
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

#OrderDict
#可以使dict的key保持顺序, 会按照插入的顺序排列,不是Key本身排序

#ChainMap
#可以把一组dict串起来并组成一个逻辑上的dict

#Counter 计数器

print('=============================base64==================================')
#用64个字符来表示任意二进制数据的方法

print('=============================struct==================================')
#struct模块来解决bytes和其他二进制数据类型的转换

print('=============================hashlib==================================')
#提供了常用的摘要算法, 如MD5,SHA1等

print('=============================hmac==================================')
#给加密的时候撒盐
#如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)。
#但实际上，把salt看做一个“口令”，加salt的哈希就是：计算一段message的哈希时，根据不通口令计算出不同的哈希。
#要验证哈希值，必须同时提供正确的口令。

print('=============================itertools==================================')
#用于操作迭代对象的函数

print('=============================contextlib==================================')
#上下文管理

print('=============================urllib==================================')
#urllib提供了一系列用于操作URL的功能。
# from urllib import request
#
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

print('=============================XML==================================')

#DOM vs SAX
#DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点
#SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件

print('=============================HTMLParser==================================')
#HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。



