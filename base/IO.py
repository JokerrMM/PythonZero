print('=======================文件读写=================')

#读文件
#标识符'r'表示读
f = open('/Users/Maitian/Desktop/JokerrMM/PythonZero/test.txt', 'r')

tx = f.read()

f.close() #关闭文件,打开后最后一定要关闭

#由于文件读写时都有可能会产生IOError, 一旦出错, 后面的f.close()就不会调用,因此为了保证能关闭文件,我们用try...finally来实现
# try:
#     f = open('/path/to/file', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

#这样写有点繁琐,所以引入了with语句来自动帮我们调用close()方法
# with open('/path/to/file','r') as f:
#     print(f.read())

print('------------二进制文件------------')
#读取二进制文件, rb = read bytes
# f2 = open('/path/to/file.jpg', 'rb')
# f2.read()

print('------------字符编码------------')
#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
#遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
# f3 = open('/path/to/test.txt', 'r', encoding='gbk', errors='ignore')

print('------------写文件-----------')
#只有在调用close()方法的时候文件才会写入磁盘, 否则就是存在内存中
# f4 = open('/path/to/file.txt', 'w')
# f4.write('Hello,world')
# f4.close()

#用with更加方便
# with open('path/to/file.txt', 'w') as f:
#     f.write('Hello, world!')

#如果要写入特定编码的文本文件,需要给open()函数传入encoding参数,将字符串自动转换成指定编码

#'w'是覆盖,如果不希望覆盖,希望追加,则用'a'(append)追加模式写入


print('=======================StringIO和BytesIO=================')
#StringIO
#在内存中读写str
from io import StringIO
f = StringIO()
print(f.write('hello')) #5

print(f.write(' ')) #1

print(f.write('world!')) #6

#getvalue()方法用于获得写入后的str
print(f.getvalue())

#如果要读取StringIO, 可以用一个str初始化StringIO,然后,像读文件一样读取
from io import StringIO
f = StringIO('Hello!\nHi\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


#BytesIO
#StringIO 操作的只能是str, 如果要操作二进制数据,就要使用BytesIO

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
#ps:写入的不是str, 而是经过UTF-8编码的bytes
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()

print('=======================操作文件和目录=================')


