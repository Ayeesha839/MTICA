#Use list comprehension to find transpose of a matrix

##m=[[1,2],[3,4],[5,6],[7,8]]
##ans=[]
##for row in range(len(m[0])): #row=0,1
##    temp=[m[col][row] for col in range(len(m))]
##    ans.append(temp)
##print(ans)

      #or
m=[[1,2],[3,4],[5,6],[7,8]]
ans=[[m[col][row] for col in range(len(m))]for row in range(len(m[0]))]
print(ans)
