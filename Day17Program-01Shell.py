Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================================ RESTART: Shell ================================
from random import*
random()
0.1339685360072138
random()
0.3688804802292336
randint(10,20)
11
random()
0.2405990591125715
randint(10,20)
13
randint(10,20)
19
help('randint')

help(randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

help('randint')

help('randint')

help(randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

for i in range(100):
    print(randint(10,20),end=',')

    
18,14,16,17,17,16,12,11,13,20,17,17,17,20,11,16,10,12,14,16,12,18,19,16,19,13,15,13,11,19,17,11,12,16,10,17,17,12,13,18,10,15,20,13,13,14,10,20,17,13,13,14,19,11,19,17,19,19,20,12,16,13,18,15,17,10,18,20,17,10,13,11,15,18,11,19,17,15,12,14,11,11,14,19,18,14,17,10,18,17,10,11,10,14,11,11,17,15,20,12,

================================ RESTART: Shell ================================
import random
random()

random.random()
0.39773287381413613

================================ RESTART: Shell ================================
import random as r
r.random()
0.27409683966894116
help(r.random)
Help on built-in function random:

random() method of random.Random instance
    random() -> x in the interval [0, 1).

r.randint(1,100)
83
help(r.randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

help(r.uniform)
Help on method uniform in module random:

uniform(a, b) method of random.Random instance
    Get a random number in the range [a, b) or [a, b] depending on rounding.

r.uniform (10,100)
87.40835092208103

================================ RESTART: Shell ================================
import random as r
r.random()
0.08331715593669697
items=[1,2,3,4,5,6,7,8,9,10]
r.shuffle(items)
items
[5, 2, 8, 4, 7, 6, 9, 10, 3, 1]
a=[12,'papaya',45,7.8,'mango']
r.shuffle(a)
a
[12, 'mango', 45, 'papaya', 7.8]
r.shuffle(a)
a
['mango', 7.8, 12, 45, 'papaya']

================================ RESTART: Shell ================================
import random as r
items=[1,2,3,4,5,6,7,8,9,10]
x=r.sample(items,3)
x
[1, 7, 5]
x=r.sample(items,3)
x
[9, 7, 8]
x=r.sample(items,2)
x
[5, 7]
