Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input("Cienījamais lietotāj, lūdzu,  ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu,  ievadi vienu skaitli: 10
10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainiigais input("Cienījamais lietotāj, lūdzu,  ievadi vienu skaitli: ")
SyntaxError: invalid syntax
>>> mans_mainiigais = input("Cienījamais lietotāj, lūdzu,  ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu,  ievadi vienu skaitli: 10
>>> vars()
{'mans_mainiigais': 10, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainiigs

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    mans_mainiigs
NameError: name 'mans_mainiigs' is not defined
>>> mans_mainiigais
10
>>> mans_mainiigais = input("Cienījamais lietotāj, lūdzu,  ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu,  ievadi vienu skaitli: 20
>>> vars()
{'mans_mainiigais': 20, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainiigais)
<type 'int'>
>>> 
>>> 
============== RESTART: /home/user/RTR105-1/tats_1_20180925.py ==============
Cienījamais lietotāj, lūdzu,  ievadi vienu skaitli: 5
>>> vars()
{'mans_mainiigais': 5, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105-1/tats_1_20180925.py', '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
============== RESTART: /home/user/RTR105-1/tats_1_20180925.py ==============
Cienījamais lietotāj, lūdzu,  ievadi vienu skaitli: 8
>>> vars()
{'mans_mainiigais': 8, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105-1/tats_1_20180925.py', '__package__': None, 'x': 64, '__name__': '__main__', '__doc__': None}
>>> vars()
{'mans_mainiigais': 8, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105-1/tats_1_20180925.py', '__package__': None, 'x': 64, '__name__': '__main__', '__doc__': None}
>>> 
============== RESTART: /home/user/RTR105-1/tats_1_20180925.py ==============
Cienījamais lietotāj, lūdzu,  ievadi vienu skaitli: 156
mans_mainiigais = 156
>>> 
============== RESTART: /home/user/RTR105-1/tats_1_20180925.py ==============
Cienījamais lietotāj, lūdzu,  ievadi vienu skaitli: 12
mans_mainiigais = 12
vai Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 12
>>> 
============== RESTART: /home/user/RTR105-1/tats_1_20180925.py ==============
Cienījamais lietotāj, lūdzu,  ievadi vienu skaitli: 12
mans_mainiigais = 12
vai Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 144
>>> 
============== RESTART: /home/user/RTR105-1/tats_1_20180925.py ==============
Cienījamais lietotāj, lūdzu,  ievadi vienu daļskaitli: 8.6549
mans_mainiigais =      8.655
vai Tu esi ievadījis skaitli:     8.6549
vēl atmiņā tagad ir arī mainīgais x =      74.9072940
>>> 
>>> 
============== RESTART: /home/user/RTR105-1/tats_1_20180925.py ==============
Cienījamais lietotāj, lūdzu,  ievadi vienu daļskaitli: 65.8888888
mans_mainiigais =     65.889
vai Tu esi ievadījis skaitli:    65.8889
vēl atmiņā tagad ir arī mainīgais x =    4341.3456673
>>> 
============== RESTART: /home/user/RTR105-1/tats_1_20180925.py ==============
Cienījamais lietotāj, lūdzu,  ievadi vienu daļskaitli: 5.1
mans_mainiigais =      5.100
vai Tu esi ievadījis skaitli:     5.1000
vēl atmiņā tagad ir arī mainīgais x =      26.0100000
>>> type(mans_mainiigais)
<type 'float'>
>>> type(mans_mainiigais)
<type 'float'>
>>> type(x)
<type 'float'>
>>> 
============== RESTART: /home/user/RTR105-1/tats_1_20180925.py ==============
Cienījamais lietotāj, lūdzu,  ievadi vienu daļskaitli: 8
mans_mainiigais =      8.000
vai Tu esi ievadījis skaitli:     8.0000
vēl atmiņā tagad ir arī mainīgais x =      64.0000000
>>> 
============== RESTART: /home/user/RTR105-1/tats_1_20180925.py ==============
Cienījamais lietotāj, lūdzu,  ievadi vienu simbolu: d

Traceback (most recent call last):
  File "/home/user/RTR105-1/tats_1_20180925.py", line 2, in <module>
    x = mans_mainiigais * mans_mainiigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
============== RESTART: /home/user/RTR105-1/tats_1_20180925.py ==============
Cienījamais lietotāj, lūdzu,  ievadi vienu simbolu: ddddddddddd

Traceback (most recent call last):
  File "/home/user/RTR105-1/tats_1_20180925.py", line 2, in <module>
    x = mans_mainiigais * mans_mainiigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
============== RESTART: /home/user/RTR105-1/tats_1_20180925.py ==============
Cienījamais lietotāj, lūdzu,  ievadi vienu simbolu: dddddddd
mans_mainiigais = dddddddd
vai Tu esi ievadījis skaitli: dddddddd
>>> 

