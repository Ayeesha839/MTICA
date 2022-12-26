Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'abc'+str(5)
'abc5'
'abc'*str(5)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    'abc'*str(5)
TypeError: can't multiply sequence by non-int of type 'str'
'abc'+5
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    'abc'+5
TypeError: can only concatenate str (not "int") to str
'abc'*5
'abcabcabcabcabc'
'abc'+5.0
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    'abc'+5.0
TypeError: can only concatenate str (not "float") to str
'abc'+float(5.0)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    'abc'+float(5.0)
TypeError: can only concatenate str (not "float") to str
str(3.0)*3
'3.03.03.0'
