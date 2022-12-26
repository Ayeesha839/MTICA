#check if string is anagram or not

def chekAnagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return 'Yes'
    else:
        return 'No'
inp=input().split()
print(chekAnagram(inp[0],inp[1]))
