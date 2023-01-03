class Rectangle:
    def __init__(self,length,width):
        assert(width>=0 and length>=0),'INVALID'
        self.length=length
        self.width=width
    def calculateArea(self):
        temp=self.length*self.width
        return temp
    def calculatePerimeter(self):
        temp=2*(self.length*self.width)
        return temp
    
w=int(input())
l=int(input())
try:
   ob=Rectangle(w,l)
   area=ob.calculateArea()
   peri=ob.calculatePerimeter()
   print('Area of Rectangle is',area)
   print('Perimeter of Rectangle is',peri)
except AssertionError as a:
    print(a)

