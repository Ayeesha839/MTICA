lst=[1,2,3,4]
it=iter(lst)# this builts an iterator object
#print(next(it))
for x in it:
    print(x,end=" ")
##or using next() function
import sys
while True:
    try:
        print(next(it))
    except StopIteration as ob:
        print(ob)
        break
        #sys.exit()  #you have to sys module for this

###o/p:1 2 3 4 
