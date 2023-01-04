Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============= RESTART: D:/pythonpractice06/day13/Day13Program-05.py ============
type(demo_yield)
<class 'function'>
x=demo_yield()
type(x)
<class 'generator'>
next(x)
code segment1 executed
49
next(x)
code segment2 executed
2
next(x)
code segment1 executed
3
next(x)
code segment4 executed
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    next(x)
StopIteration
