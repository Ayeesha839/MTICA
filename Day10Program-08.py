fo1=open(r"D:/pythonpractice06/day10/data10a.txt","r")
fo2=open(r"D:/pythonpractice06/day10/test.txt",'w+')

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("File copied")
