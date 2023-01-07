def result(s1,s2):
    return [int(i)+int(j) for i,j in zip(s1,s2)]
inp1=input().strip().split()
inp2=input().strip().split()
print(*result(inp1,inp2))

##o/p:11 22 33 44 55
##    1 2 3 4 5
##    12 24 36 48 60
