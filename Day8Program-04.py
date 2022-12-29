def div(a,b):
    assert(b!=0),"Division by zero is not defined"
    return a/b
try:
    print(div(55,0))
except Exception as ob:
    print(ob)
try:
    print(div(20,3))
except Exception as ob:
    print(ob)
try:
    print(div(100,20))
except Exception as ob:
    print(ob)

print("Thank You")
