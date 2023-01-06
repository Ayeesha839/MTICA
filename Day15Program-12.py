def outer():
    print('outer function')
    def inner():
        print('inner function')
    inner()
outer()

##o/p:outer function
##    inner function
