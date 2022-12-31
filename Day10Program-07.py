fo=open(r"D:\pythonpractice06\day10\data10a.txt","a")
for i in range(5):
    inpstr=input("Enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("Write to file")
