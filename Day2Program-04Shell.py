Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================================ RESTART: Shell ================================
a="today"
b=input()
'computing'
b[0]
"'"
>>> b[2]
'o'
>>> c=computing
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    c=computing
NameError: name 'computing' is not defined
>>> b=input()
computing
>>> b[0]
'c'
>>> b[2]
'm'
>>> b[7]
'n'
>>> b[-1]
'g'
>>> b[-7]
'm'
>>> b[3:6]
'put'
>>> b[2:]
'mputing'
>>> b[6:]
'ing'
>>> b[::2]
'cmuig'
>>> b[1::3]
'oun'
>>> b[::-1]
'gnitupmoc'
