'''calculate volume and surface area of cylinder
pi=3.14159 and round out 4 decimal places
input:2
      10
output:125.6636
       150.7963
       '''
pi=3.14159
radius=int(input())
height=int(input())
base_area=pi*radius**2
volume=round(base_area*height,4)
surface_area=round(2*base_area+2*pi*radius*height,4)
#print("volume is",volume,"surface_area is",surface_area)
print(volume)
print(surface_area)
