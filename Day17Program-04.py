import sys
print("Coming throgh stdout")
#stdout is saved
save_stdout=sys.stdout
print('sys.stdout:',sys.stdout)
fh=open(r"D:\pythonpractice06\day17\test.txt","w")
sys.stdout=fh
print("This line goes to test.txt")
print(input())
#return to normal:
sys.stdout=save_stdout
fh.close()

##o/p:
##Coming throgh stdout
##sys.stdout: <idlelib.run.StdOutputFile object at 0x000001B2C3955030>
##hello everyone
