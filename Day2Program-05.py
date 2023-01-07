'''palindrome or not
i/p-535
o/p-is palindrome
i/p-234
o/p-is not palindrome'''
a=input()
if a==a[::-1]:
    print(a,"is palindrome")
else:
    print(a,"is not a palindrome")
