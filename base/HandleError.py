print('=======================错误处理=================')

#错误处理
#try...except...finally的处理机制

#try
# 如果try执行出错,则后续代码不会继续执行,而是直接跳转至错误处理代码,即except语句块,执行完except后,如果有finally语句块,则执行finally语句块,执行完毕
try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

#可以有多个except来捕获不同类型的错误
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError: e')
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')



#调用栈
#如果错误没有被捕获,它就会一直往上抛,最后被python解释器捕获,打印一个错误信息,然后程序退出
#出错的时候,一定要分析错误的调用栈信息,才能定位错误的位置
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar('0')
#
# main()


#记录错误 logging模块
#程序打印完错误信息后会继续执行,并正常退出,通过配置,logging可以把错误记录到日志文件里
# import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('END')


#抛出错误
# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' %s)
#     return  10 / n
#
# foo('0')


#练习
from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

# main()


print('=======================调试=================')

#print() 最大的坏处是将来还得删掉它

#断言 assert
#凡是用print()的地方都可以使用断言来替代它, 如果断言失败, assert语句本身就会抛出AssertionError
#启动python解释器时可以用-O参数来关闭assert

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n

foo('0')

#logging
#logging不会抛出错误,而且可以输出到文件
#logging的好处,它可以允许你指定记录信息的级别, 有debug, info, warning, error等几个级别


#pdb
#断点调试,单步调试

print('=======================单元测试=================')

pass


print('=======================文档测试=================')
#re模块
pass
