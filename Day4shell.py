  Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'hello'"world"'python'
'helloworldpython'
a="hello""world""python"
a
'helloworldpython'
a="hello","world",'python'
a
('hello', 'world', 'python')
type(a)
<class 'tuple'>
b=2
type(b)
<class 'int'>
b=(2)
type(b)
<class 'int'>
c=(2,)
type(c)
<class 'tuple'>
f=('hi')
type(f)
<class 'str'>
d=("hello")
type(d)
<class 'str'>
j=("hello",)
type(j)
<class 'tuple'>
i=2,7,'fgh',"sdf",3+2j
type(i)
<class 'tuple'>
i=[2,7,'fgh',"sdf",3+2j]
type(i)
<class 'list'>
lst=[2,8,4.7,'f',"fgh"]
type(lst)
<class 'list'>


lst.append(10)
lst
[2, 8, 4.7, 'f', 'fgh', 10]
lst.append(10)
lst
[2, 8, 4.7, 'f', 'fgh', 10, 10]
lst.append("hello")
lst.append("welcome")
lst
[2, 8, 4.7, 'f', 'fgh', 10, 10, 'hello', 'welcome']
lst.clear()
lst
[]

lst=[2, 8, 4.7, 'f', 'fgh', 10, 10, 'hello', 'welcome']
lst
[2, 8, 4.7, 'f', 'fgh', 10, 10, 'hello', 'welcome']
lst.count()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    lst.count()
TypeError: list.count() takes exactly one argument (0 given)
lst.count(10)
2
lst.count(8)
1
lst.count('a')
0

len.lst
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    len.lst
AttributeError: 'builtin_function_or_method' object has no attribute 'lst'
len(lst)
9
print(lst(id))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(lst(id))
TypeError: 'list' object is not callable
print(id(lst))
1577686487104
lst1=[2,'i',"eryt",3.8]
lst1
[2, 'i', 'eryt', 3.8]
print(id(lst1))
1577680238784
print(id(lst),id(lst1))
1577686487104 1577680238784

lst
[2, 8, 4.7, 'f', 'fgh', 10, 10, 'hello', 'welcome']
lst[:]
[2, 8, 4.7, 'f', 'fgh', 10, 10, 'hello', 'welcome']
lst[1:]
[8, 4.7, 'f', 'fgh', 10, 10, 'hello', 'welcome']

lst[3:]
['f', 'fgh', 10, 10, 'hello', 'welcome']
lst5
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    lst5
NameError: name 'lst5' is not defined. Did you mean: 'lst'?
lst
[2, 8, 4.7, 'f', 'fgh', 10, 10, 'hello', 'welcome']
lst[3:]
['f', 'fgh', 10, 10, 'hello', 'welcome']

lst
[2, 8, 4.7, 'f', 'fgh', 10, 10, 'hello', 'welcome']
lst.append(('fi',4,5.2))
lst
[2, 8, 4.7, 'f', 'fgh', 10, 10, 'hello', 'welcome', ('fi', 4, 5.2)]
lst.append(["as",6,3.0])
lst
[2, 8, 4.7, 'f', 'fgh', 10, 10, 'hello', 'welcome', ('fi', 4, 5.2), ['as', 6, 3.0]]
lst[-1]
['as', 6, 3.0]

lst[4]
'fgh'

lst
[2, 8, 4.7, 'f', 'fgh', 10, 10, 'hello', 'welcome', ('fi', 4, 5.2), ['as', 6, 3.0]]
del lst[3:5]
lst
[2, 8, 4.7, 10, 10, 'hello', 'welcome', ('fi', 4, 5.2), ['as', 6, 3.0]]
del lst[6:7]
lst
[2, 8, 4.7, 10, 10, 'hello', ('fi', 4, 5.2), ['as', 6, 3.0]]
del lst[6:8]
lst
[2, 8, 4.7, 10, 10, 'hello']
del lst[8:8]
lst
[2, 8, 4.7, 10, 10, 'hello']

lst.extend(4,5.6,"ki",'hji'))
SyntaxError: unmatched ')'
lst.extend(4,5.6,"ki",'hji')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    lst.extend(4,5.6,"ki",'hji')
TypeError: list.extend() takes exactly one argument (4 given)
lst.extend((4,5.6,"ki",'hji'))
lst
[2, 8, 4.7, 10, 10, 'hello', 4, 5.6, 'ki', 'hji']
lst.extend([3,1]))
SyntaxError: unmatched ')'
lst.extend([3,1])
lst
[2, 8, 4.7, 10, 10, 'hello', 4, 5.6, 'ki', 'hji', 3, 1]

lst.index(8)
1
lst.index('hello')
5

lst.insert([4,456])
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    lst.insert([4,456])
TypeError: insert expected 2 arguments, got 1
lst.insert([4,456],'di')
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    lst.insert([4,456],'di')
TypeError: 'list' object cannot be interpreted as an integer
lst.insert((4,456))
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    lst.insert((4,456))
TypeError: insert expected 2 arguments, got 1
lst.insert((4,456),'fr')
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    lst.insert((4,456),'fr')
TypeError: 'tuple' object cannot be interpreted as an integer
lst.insert(4,456,'fr')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    lst.insert(4,456,'fr')
TypeError: insert expected 2 arguments, got 3

lst
[2, 8, 4.7, 10, 10, 'hello', 4, 5.6, 'ki', 'hji', 3, 1]
lst.insert(0,'c')
lst
['c', 2, 8, 4.7, 10, 10, 'hello', 4, 5.6, 'ki', 'hji', 3, 1]
lst.insert('hi',"fi")
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    lst.insert('hi',"fi")
TypeError: 'str' object cannot be interpreted as an integer
lst.insert('hi','fi')
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    lst.insert('hi','fi')
TypeError: 'str' object cannot be interpreted as an integer


lst.insert(4,"hi")
lst
['c', 2, 8, 4.7, 'hi', 10, 10, 'hello', 4, 5.6, 'ki', 'hji', 3, 1]
lst.insert(4,"leo")
lst
['c', 2, 8, 4.7, 'leo', 'hi', 10, 10, 'hello', 4, 5.6, 'ki', 'hji', 3, 1]
lst.insert(6,"jeo")
lst
['c', 2, 8, 4.7, 'leo', 'hi', 'jeo', 10, 10, 'hello', 4, 5.6, 'ki', 'hji', 3, 1]

help of list
SyntaxError: invalid syntax
help(list)

lst.pop(2)
8
lst
['c', 2, 4.7, 'leo', 'hi', 'jeo', 10, 10, 'hello', 4, 5.6, 'ki', 'hji', 3, 1]
lst.pop('hello')
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    lst.pop('hello')
TypeError: 'str' object cannot be interpreted as an integer
lst.pop(1)
2

lst.remove(2)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    lst.remove(2)
ValueError: list.remove(x): x not in list


append
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    append
NameError: name 'append' is not defined


#append
#clear
#count
#len
#del
#remove
#insert
#pop
#sort


a='today is saturday'
a.replace('at','****')
'today is s****urday'
a
'today is saturday'
a.replace('at','****')
'today is s****urday'
a.replace('****','at')
'today is saturday'
a='computer'
a=a.replace('put','python')
a
'compythoner'
a
'compythoner'
