#Extract all DIGITS from an input string
#use list comprehension

##inp=input()
##ans=[]
##for i in inp:
##    if i in '0123456789':
##        ans.append(i)
##print(*ans)

       #or

inp=input()
ans=[i for i in inp if i in '0123456789']
print(*ans)
