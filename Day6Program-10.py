###numbers 1-1000 divisible by 8
##ans=[]
##for i in range(1,1001):
##    if i%8==0:
##        ans.append(i)
##print(ans)

##########or###########

##print([i for i in range(1,1001) if i%8==0])


#########or##########


ans=[i for i in range(1,100) if i%8==0]
print(ans)
