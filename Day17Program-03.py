import sys
print(sys.argv)
for i in range(len(sys.argv)):
    if i==0:
        print("function name:{0}".format(sys.argv[0]))
    else:
        print("{0}.argument:{1}".format(i,sys.argv[i]))

##o/p:['D:/pythonpractice06/day17/Day17Program-03.py']
##    function name:D:/pythonpractice06/day17/Day17Program-03.py


####command prompt o/p:
##C:\Users\admin>d:
##
##D:\>cd pythonpractice06
##
##D:\pythonpractice06>cd day17
##
##D:\pythonpractice06\day17>python Day17Program-03.py
##['Day17Program-03.py']
##function name:Day17Program-03.py
##
##D:\pythonpractice06\day17>python Day17Program-03.py priyanka ayeesha mca mtica
##['Day17Program-03.py', 'priyanka', 'ayeesha', 'mca', 'mtica']
##function name:Day17Program-03.py
##1.argument:priyanka
##2.argument:ayeesha
##3.argument:mca
##4.argument:mtica
