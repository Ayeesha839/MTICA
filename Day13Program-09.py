####find squares
def squares(x=0):
    while x<10:
        x=x+1
        yield x*x
for m in squares():
    print(m)

    #or
def squares(x=0):
    while x<10:
        x=x+1
        yield x*x
yieldList=[m for m in squares()]
print(yieldList)
   
       ##or
#Materialized list from generator using list()
def squares(x=0):
    while x<10:
        x=x+1
        yield x*x
yieldList=list(squares())
print(yieldList)
        

      ####find cubes
def cubes(x=0):
    while x<10:
        x=x+1
        yield x*x*x
for m in cubes():
    print(m)
