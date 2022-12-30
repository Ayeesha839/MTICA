
'''i/p:5
   o/p:1
       1 2
       1 2 3
       1 2 3 4
       1 2 3 4 5 '''
    
def printSeries(n):
    for i in range(1,n+1):
        num=1
        print()
        for j in range(i):
            print(num,end=' ')
            num+=1
    return None
inpNum=int(input())
printSeries(inpNum)
