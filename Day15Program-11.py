##nonlocal

##first function
def f():
    x=10
    print('id(x)in f outer:',id(x))
    #nested function
    def g():
        nonlocal x
        x=15
        print('id(x)in g inner:',id(x))
    g()
    print(x)
f()

##o/p:id(x)in f outer: 140711997457480
##    id(x)in g inner: 140711997457640
##    15
    
