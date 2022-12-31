def fun(str1):
    print(str1)
    return
fun("I'm first call to user defined function!")
fun("Again second call to the same function")

def printme(str1,n):
    n[0]='Prasad'
    print(str1,n)
    return

x=['Ganguly','Manohar']
printme("Wakeup",x)
print('x:',x)
