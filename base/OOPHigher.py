print('=======================使用__slots__=================')
#我们可以动态给实例添加属性或者方法
#__slots__变量, 可以限制该class实例能添加的属性

class Student(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

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

s1= Student1()
s1.score = 60
s1.score = 999


print('=======================多重继承=================')

