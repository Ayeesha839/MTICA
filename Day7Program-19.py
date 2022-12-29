Lst1=[11,22,33,44,55]
Lst2=[1,2,3,4,5]
# if add list and list 2:[12,24,36,48,55]
def add(a,b):
    return a+b
ans=list(map(add,Lst1,Lst2))
print(Lst1)
print(Lst2)
print(ans)

      #or
Lst1=[11,22,33,44,55]
Lst2=[1,2,3,4,5]
ans=list(map(lambda a,b:a+b,Lst1,Lst2))
print(ans)
