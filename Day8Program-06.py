num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
try:
    res=num1/num2 #Execute with num2=non zero and zero#4
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print(num1,'/',num2,'=',res)
print('Thanks')
