ans=[]
for i in range(100,111):
    temp=[]
    for j in range(1,10):
        if i%j==0:
            temp.append(j)
    ans.append([i,max(temp)])
print(ans)
