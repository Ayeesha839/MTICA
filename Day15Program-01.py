'''create a class with instance attributes
write a program for create a Vehicle class
with max_speed and mileage  are instance attributes'''
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
modelX=Vehicle(240,18)
print(modelX.max_speed,modelX.mileage)
    

######o/p-240 18
