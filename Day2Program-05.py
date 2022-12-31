'''palindrome or not'''
a=input()
if a==a[::-1]:
    print(a,"is palindrome")
else:
    print(a,"is not a palindrome")
