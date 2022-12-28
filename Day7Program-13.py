lst=[10,15,2,25,30,3,40,4]
ans=[]
for i in lst:
    if i**2>50:
        ans.append(i**2)
print(ans)

       #or

lst=[10,15,2,25,30,3,40,4]
ans=[i**2 for i in lst if i**2>50]
print(ans)
