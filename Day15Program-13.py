def outer():
    message='outer function'
    print(message)
    def inner():
        print(message)
    inner()
outer()

##o/p:outer function
##    outer function
