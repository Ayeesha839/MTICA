'''calculate radius of circle
input:
15
output:
2.1850988
input:
35
output:
3.337792
input:
5
output:
invalid area
'''
inpArea=int(input("enter area of circle:"))      
if inpArea<0:
      print('Invalid area')
else:
      pi=3.14159
      radius=round(inpArea/pi)**(1/2),6)
      print("for the given area",inpArea,"radius is:",radius)
      print("Area:"+str(inpArea),"radius:"+str(radius))
    
