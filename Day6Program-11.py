#find all the numbers from 950-1001 that have a 4 in them.
##ans=[]
##for i in range(950,1001):
##    if '4' in str(i):
##        ans.append(i)
##print(ans)
##
           #or

####print([i for i in range(950,1001) if '4' in str(i)])


        #or

ans=[i for i in range(950,1001) if '4' in str(i)]
print(ans)
