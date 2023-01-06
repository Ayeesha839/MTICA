'''write a program for calculate LCM of two numbers
i/p-20,30
O/P-60
'''
def findLCM(n1,n2):
    if n1<0 or n2<0:
        return "INVALID"
    if n1>n2:
        n1,n2=n2,n1
    i=n2
    while True:
        if i%n1==0 and i%n2==0:
            return i
        else:
            i+=1
    return None

print("Enter two values")
a=int(input())
b=int(input())
print(findLCM(a,b))

##o/p:
##Enter two values
##20
##47
##940
