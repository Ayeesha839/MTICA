#remove empty strings
lst=["Sedan", "SUV", "", "", "Pickup",'',' ']
ans=[]
for i in lst:
    if i:
       ans.append(i)
print(ans)

      #or

lst=["Sedan", "SUV", "", "", "Pickup",'',' ']
ans=[i for i in lst if i]
print(ans)
