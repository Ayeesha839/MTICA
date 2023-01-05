#super refers to the parent class

class A:
    def first_method(self):
        print("Method of class A...")
#B().first_method()
class B(A):
    def first_method(self):
        print("Method of class B...")
        super().first_method()#calls the first_method()of
                       #the superclass "A"
        
ob=B()
ob.first_method()
