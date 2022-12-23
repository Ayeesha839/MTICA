inpArea=int(input("Enter tha area of the circle:"))
if inpArea<0:
    print('Invalid area')
else:
    pi=3.14159
    radius=round((inpArea/pi)**(1/2),6)
    print("for the given area",inpArea,"radius is:",radius)
    print("Area:"+str(inpArea),"radius:"+str(radius))   
