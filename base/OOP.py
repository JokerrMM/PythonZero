#面向对象的设计思想是抽象出类(class),然后根据类(class)创建实例(Instance)
#封装,继承和多态是面向对象的三大特点

print('=======================类和实例=================')
#类
class Student1(object):
    pass

bart = Student1()
print(bart)
print(Student1)

#可以自由地给一个实例变量绑定属性,比如给bart绑定一个name属性,但是一般不推荐这么做,推荐是在定义类的时候把一些
#我们认为必须绑定的属性给强制填写进去,通过定义一个特殊的__init__方法,在创建实例的时候,就把name,score等属性绑上去
bart.name = 'Bart Simpson'
print(bart.name)


class Student(object):
#__init__方法的第一个参数永远是self,表示创建的是实例本身,因此,在__init__方法内部,就可以把各种属性绑定到self,因为self就指向创建的实例本身
#有了__init__方法,在创建实例的时候,就不能传入空的参数了,必须传入与__init__方法匹配的参数,但是self不需要传,python解释器会自己把实例变量传进去
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))

s1 = Student('June', 69)
print(s1.print_score())

print('=======================访问限制=================')
#实例的变量名如果以__开头,就变成了一个私有变量(private),就只有类的内部可以访问,外部将不能访问
class Student2(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s %s' % (self.__name, self.__score))

s2 = Student2('Mary', 100)
print(s2.print_score())

#但是,如果外部代码要获取name和score方法,就需要给类增加get_name和get_score这样的方法
#如果外部代码要修改name和score方法,就需要给类增加set_name和set_score这样的方法

class Student3(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


s3 = Student3('Jack', 55)
s3.set_name('Nancy')
print(s3.get_name())
s3._Student3__name = 'QA'
print(s3.get_name())

#注意: 在python中, 变量名类似__xxx__的,就是以双下划线开头和结束的,是特殊变量,是可以直接访问的,不是private变量
#还有就是,_name虽然可以直接访问,但是按照约定成熟的规定,当我们看到这样的变量的时候,意思是'虽然我可以被访问,但是,请把我视为私有变量,不要随意访问'
#__name其实还是可以访问的, 通过_Student__name, 但是不推荐


print('=======================继承与多态=================')
#当子类和父类都存在相同的run()方法时,子类的run()就会覆盖了父类了run()
class Animal(object):
    def run(self):
        print('Animal is running....')

class Dog(Animal):
    def run(self):
        print('Dog is running....')

class Cat(Animal):
    def run(self):
        print('Cat is running....')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

#继承可以把父类的所有功能都直接拿过来,这样就不必从零做起,子类只需要新增自己特有的方法,也可以把父类不适合的方法覆盖重写
#动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的

print('=======================获取对象信息=================')
#使用type()函数来判断对象类型

#返回的是对应的Class类型
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))

#使用isinstance()

#要判断class的类型,可以使用isinstance()函数
#isinstance()判断的是一个对象是否是该类型本身,或者位于该类型的父继承链上
#总是优先使用isinstance()判断类型,可以将指定类型及其子类'一网打尽'

a = Animal()
b = Dog()
c = Cat()

print(isinstance(c, Cat)) #True
print(isinstance(c, Animal)) #Ture
print(isinstance(a, Dog)) #False
print(isinstance(c, Dog)) #False


#使用dir()

#如果要获得一个对象的所有属性和方法,可以使用dir()函数,它返回一个包含字符串的list
print(dir(a))

print('=======================实例属性和类属性=================')

#给实例绑定属性的方法是通过实例变量, 或者通过self变量
class Student4(object):
    def __init__(self, name):
        self.name = name

s4 = Student4('Bob')
s4.score = 90

#如果类本身需要绑定一个属性,可以直接在class中定义属性,这种就是类属性,归类所有
#千万不要对实例属性和类属性使用相同的名字,因为相同名称的实例属性将屏蔽掉类属性,但是当你删除实例属性后,再使用相同的名称,访问到的将是类属性
