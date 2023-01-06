message='global scope'
def outer():
    def inner():
        print(message)
    inner()
outer()

##o/p:global scope
