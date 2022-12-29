def factorial(n):
    assert(n>=0),"Factorial of negative number is not defined"
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
try:
    print(factorial(3))
except Exception as ob:
    print(ob)
try:
    print(factorial(-3))
except Exception as ob:
    print(ob)
try:
    print(factorial(0))
except Exception as ob:
    print(ob)

print("Thank You")
