def chekPalindrome(inp):
    if inp==inp[::-1]:
        return 'Yes'
    else:
        return 'No'
inp=input()
print(chekPalindrome(inp))
