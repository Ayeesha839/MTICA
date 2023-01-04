'''program to create generator that
generates cubes of upto 1000using yield
once it reaches  1000,it will stops'''

def calculatorCubic():
    i=1
    while True:
        yield i*i*i
        i+=1
for num in calculatorCubic():
    if num>1000:
        break
    print(num)




####find cubes
##def cubes(x=0):
##    while x<10:
##        x=x+1
##        yield x*x*x
##for m in cubes():
##    print(m)
