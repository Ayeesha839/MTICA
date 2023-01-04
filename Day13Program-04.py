def PrintAdd(a,b):
    return a+b
def PrintSub(a,b):
    return a-b
def PrintMul(a,b):
    return a*b
def PrintDiv(a,b):
    return a/b
def choice():
    print("+:Addition");print("-:Substraction");
    print("*:Multiplication");print("/:Division");
    print("q:Quit");
    return
ArithmeticSelect={"+":PrintAdd,"-":PrintSub,"*":PrintMul,"/":PrintDiv}
while True:
    choice()
    selection=input("Select an Arithmetic operation:")
    if selection=='q' or selection=='Q':break
    if ((selection=='+') or (selection=='-')or
              (selection=='*') or (selection=='/')):
        n1=int(input("Enter first num:"))
        n2=int(input("Enter first num:"))
        z=ArithmeticSelect[selection](n1,n2)
        print(n1,selection,n2,'=',z)
               
        
    
    
