Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================================ RESTART: Shell ================================
a=set()
type(a)
<class 'set'>
b={8}
type(b)
<class 'set'>
c={'Emma','John','Jimmy'}
type(c)
<class 'set'>
d={}
type(d)
<class 'dict'>
a={1,2,3,4,5}
b={4,5,6,7,8,9}
a+b
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a={1,2,3,4,5}
b={4,5,6,7,8}
a+b
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a.intersection(b)
{4, 5}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
s='today is monday and we learning dictionary'
a=list(s)
a
['t', 'o', 'd', 'a', 'y', ' ', 'i', 's', ' ', 'm', 'o', 'n', 'd', 'a', 'y', ' ', 'a', 'n', 'd', ' ', 'w', 'e', ' ', 'l', 'e', 'a', 'r', 'n', 'i', 'n', 'g', ' ', 'd', 'i', 'c', 't', 'i', 'o', 'n', 'a', 'r', 'y']
set(a_)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    set(a_)
NameError: name 'a_' is not defined. Did you mean: 'a'?
a=[34,798,28,46,34]
a={34,798,28,46,34}
b=set(a)
b
{46, 34, 28, 798}
b=list(set(a))
