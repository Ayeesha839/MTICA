class Complex:
    def __init__(self,real,image):
        self.real=real
        self.image=image
    def __add__(self,obj):
        temp=self.real+obj.real,self.image+obj.image
        return temp
    def __str__(self):
        return(self.real,self.image)
obj1=Complex(3,5)
obj2=Complex(2,1)
obj3=obj1+obj2
print(obj3)
#print(obj4)

    
