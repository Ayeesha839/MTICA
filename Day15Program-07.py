'''pythonprogram to calculate find factor of two numbers '''
def findFactor(n):
    temp=[]
    for i in range(1,n+1):
        if n%i==0:
            temp.append(i)
    return temp
a=int(input())
print(*findFactor(a))

##o/p:30
##1 2 3 5 6 10 15 30
