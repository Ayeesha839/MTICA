'''write a python program for remove special characters
excluding alphabets and numerics and special characters.
INPUT:
fun_Add()
OUTPUT:
funAdd
INPUT:
lucy.hi@gmail.com
OUTPUT:
lucyhigmailcom
INPUT:
-783.56 
OUTPUT:
 78356  '''
   ###using list
def removeSpecialChar(s):
    ans=[]
    for i in s:
        if i in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
           ans.append(i)
    return ''.join(ans)
inp=input()
print(removeSpecialChar(inp))

   ### (or)using string
def removeSpecialChar(s):
    ans=[]
    for i in s:
        if (ord(i) in range(65,91) or ord(i) in range(97,123)
        or ord(i) in range(48,57)):
            ans.append(i)
    return ''.join(ans)
inp=input()
print(removeSpecialChar(inp))


