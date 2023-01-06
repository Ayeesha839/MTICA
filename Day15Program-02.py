class Vector3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,ob):
        return Vector3D(self.x+ob.x,self.y+ob.y,self.z+ob.z)
first=Vector3D(11,22,33)
second=Vector3D(1,2,3)
result=first+second
print(result.x,result.y,result.z)


##o/p:12 24 36
