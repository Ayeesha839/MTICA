class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __mul__(self,obj):
        temp=(self.real*obj.real-self.img*obj.img,
              self.real*obj.img+self.img*obj.real)
        return temp
    def __str__(self):
        return(self.real,self.img)
obj1=Complex(3,5)
obj2=Complex(2,1)
obj3=obj1*obj2
print(obj3)


    
