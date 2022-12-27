#Remove all the vowels in the string

####string='''I am pursuing MCA'''
####ans=[]
####for i in string:
####    if i not in 'AEIOUaeiou':
####        ans.append(i)
####print(*ans)

       #or

string='''I am pursuing MCA'''
ans=[i for i in string if i not in 'AEIOUaeiou']
print(*ans)
