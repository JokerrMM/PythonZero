print('=======================使用__slots__=================')
#我们可以动态给实例添加属性或者方法
#__slots__变量, 可以限制该class实例能添加的属性

class Student(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 25111
# s.score = 991111

#由于'score'没有被放到__slots__中,所以不能绑定score属性,试图绑定score将得到AttributeError的错误
#__slots__定义的属性仅对当前实例起作用,对继承的子类是不起作用的




print('=======================使用@property=================')
#@property  是一个装饰器
#如果只定义了getter方法,不定义setter方法,则该属性为只读属性

class Student1(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# s1= Student1()
# s1.score = 60
# s1.score = 999


print('=======================多重继承=================')
#多重继承,就是可以同时继承多个类


print('=======================定制类=================')

#__str__()
#这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。

class Student2():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student ojbect (name: %s)' % self.name

    __repr__ = __str__
#而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

print(Student2('Michael'))


#__iter__
#如何让类可以被用于for...in循环,实现__iter__()方法就可以,该方法返回一个迭代对象,然后,py的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值
#直到遇到StopIteration错误时退出循环

class Fib(object):
    def __int__(self):
        self.a, self.b == 0, 1 #初始化两个计数器a,b

    def __iter__(self):
        return self #实例本身就是迭代对象,故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b #计算下一个
        if self.a > 10000:  #退出循环的条件
            raise StopIteration()
        return self.a #返回下一个值

#__getitem__
class Fib1(object):
    def __getitem(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


# __getattr__
class Student3(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

#此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：





