Lst1=[11,22,33,44,55]
Lst2=[1,2,3,4,5,6,7,8]
Lst3=[5,6,5,2,1,3,2,3] #11*1+5
print(Lst1)
print(Lst2)
print(Lst3)
ans=list(map(lambda a,b,c:a*b+c,Lst1,Lst2,Lst3))
print(ans)
