#inherit is a way to share functionality between classes.
class Animal:   #super class
    def __init__(self,name,color):
        self.name=name
        self.color=color
#cat and dog are sub classes
class Cat(Animal):  #to inherit a class from 
    def mew(self):
        print("Cat meows")
class Dog(Animal):
    def bark(self):
             print("Woof")
if __name__=="__main__":
    print(__name__)
    pet1=Dog("tommy","brown")
    pet2=Cat("lucy","white")
    pet1.bark()
    pet2.mew()
    print(pet1.name)
    print(pet2.name)
             

    
