#Extract all vowels from an input string
#use list comprehension

string=input()
ans=[]
for i in string:
    if i in 'AEIOUaeiou':
        ans.append(i)
print(*ans)
