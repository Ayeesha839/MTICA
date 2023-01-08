from random import *
print(random())
print(randint(1,100))
print(uniform(1,10))

items=[1,2,3,4,5,6,7,8,9,10]
shuffle(items)
print(items)


x=sample(items,3)
print("x=",x)
print(x[0])
y=sample(items,4)
print(y)

##o/p:
##0.3776300322295896
##49
##7.6305436361950045
##[3, 6, 4, 8, 2, 5, 7, 1, 10, 9]
##x= [9, 1, 4]
##9
##[9, 2, 6, 5]
      
