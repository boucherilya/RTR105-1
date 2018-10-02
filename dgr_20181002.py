Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> print(98.6)
98.6
>>> print('Hello world')
Hello world
>>> x=12.2
>>> y=14
>>> x=100
>>> x1q3z9ocd = 35
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd
>>> print(x1q3z9afd)
12.5
>>> x1q3z9ocd = 35.0
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd
>>> print(x1q3z9afd)
12.5
>>> x1q3z9ocd = 35.0
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd
>>> print(x1q3p9afd)
437.5
>>> a = 35.0
>>> b = 12.50
>>> c = a * b
>>> c
437.5
>>> hours = 35.0
>>> rate = 12.50
>>> pay = hours * rate
>>> print(pay)
437.5
>>> x = 2
>>> x = x + 2
>>> print(x)
4
>>> x = 3.9 * x * (1 - x)
>>> print(x)
-46.8
>>> x = 0.936
>>> x = 3.9 * x * (1-x)
>>> print(x)
0.2336256
>>> xx = 2
>>> xx = xx + 2
>>> print(xx)
4
>>> yy = 440 * 12
>>> print(yy)
5280
>>> zz = yy / 1000
>>> print (zz)
5
>>> print(zz)
5
>>> jj = 23
>>> kk = jj % 5
>>> print(kk)
3
>>> print(4 ** 3)
64
>>> x = 1 + 2 * 3 - 4 / 5 ** 6
>>> x = 1 + 2 ** 3 / 4 * 5
>>> print(x)
11
>>> ddd = 1 + 4
>>> print(ddd)
5
>>> eee = 'hello' + 'there'
>>> print(eee)
hellothere
>>> eee = 'hello ' + 'there'
>>> eee = eee + 1

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    eee = eee + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> type('hello')
<type 'str'>
>>> type(1)
<type 'int'>
>>> xx = 1
>>> type (xx)
<type 'int'>
>>> temp = 98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99) + 100)
199.0
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> print(9/2)
4
>>> print(99/100)
0
>>> print(10.0/2.0)
5.0
>>> print(99.0/100.0)
0.99
>>> sval = '123'
>>> type(sval)
<type 'str'>
>>> print(sval + 1)

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print(sval + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival + 1)
124
>>> nsv = 'hello bob'
>>> niv = int(nsv)

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    niv = int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam = input('Who are you? ')
Who are you? 

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    nam = input('Who are you? ')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> print('Welcome',ArithmeticError nam)
SyntaxError: invalid syntax
>>> nam = input('Who are you? ')
Who are you? print('Welcome' Ilya)

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    nam = input('Who are you? ')
  File "<string>", line 1
    print('Welcome' Ilya)
        ^
SyntaxError: invalid syntax
>>> nam = input('Who are you? ')
Who are you? yyyyy

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    nam = input('Who are you? ')
  File "<string>", line 1, in <module>
NameError: name 'yyyyy' is not defined
>>> nam = raw_input('Who are you? ')
Who are you? yyyy
>>> inp - raw_input('Europe floor?')

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    inp - raw_input('Europe floor?')
NameError: name 'inp' is not defined
>>> inp - input('Europe floor?')

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    inp - input('Europe floor?')
NameError: name 'inp' is not defined
>>> usf = int(inp) + 1

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    usf = int(inp) + 1
NameError: name 'inp' is not defined
>>> inp = raw_input('Europe floor?')
Europe floor?
>>> usf = int(inp) + 1

Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    usf = int(inp) + 1
ValueError: invalid literal for int() with base 10: ''
>>> usf = raw_int(inp) + 1

Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    usf = raw_int(inp) + 1
NameError: name 'raw_int' is not defined
>>> usf = int(inp) + 1

Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    usf = int(inp) + 1
ValueError: invalid literal for int() with base 10: ''
>>> inp = raw_input('Europe floor?')
Europe floor? usf = int(inp) + 1
>>> print('US floor', usf)

Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    print('US floor', usf)
NameError: name 'usf' is not defined
>>> inp = raw_input('Europe floor?')
Europe floor? usf = raw_int(inp) + 1
>>> print('US floor', usf)

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    print('US floor', usf)
NameError: name 'usf' is not defined
>>> inp = raw_input('Europe floor?')
Europe floor?1
>>> usf = int(inp) + 1
>>> print('US floor', usf)
('US floor', 2)
>>> name = raw_input('Enter file:')
Enter file: history_20180925.txt
>>> handle = open(name, 'r')

Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    handle = open(name, 'r')
IOError: [Errno 2] No such file or directory: ' history_20180925.txt'
>>> hours = 35
>>> rate = 2.75
>>> pay = hours * rate
>>> print(pay)
96.25
>>> 
