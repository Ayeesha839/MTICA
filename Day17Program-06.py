import datetime
obj=datetime.datetime.now()
print(type(obj))
print("-"*25)
print(obj)
print(obj.year)
print(obj.month)
print(obj.day)
print(obj.hour)
print(obj.minute)
print(obj.second)
str1=str(obj.hour)+':'+str(obj.minute)+':'+str(obj.second)
print(str1)
print("-"*25)
print("1 week ago it was:",obj-datetime.timedelta(weeks=1))
print("100 week ago it was:",   obj-datetime.timedelta(days=100))
print("1 week from now it will be:",obj+datetime.timedelta(weeks=1))
print("1000 days later it will be:",obj+datetime.timedelta(days=100))
bday_lucy=datetime.datetime(2001,5,21)
print("-"*25)
print("Birthday in...",obj-bday_lucy)
print("-"*25)

##o/p:
##<class 'datetime.datetime'>
##-------------------------
##2023-01-08 12:11:03.115645
##2023
##1
##8
##12
##11
##3
##12:11:3
##-------------------------
##1 week ago it was: 2023-01-01 12:11:03.115645
##100 week ago it was: 2022-09-30 12:11:03.115645
##1 week from now it will be: 2023-01-15 12:11:03.115645
##1000 days later it will be: 2023-04-18 12:11:03.115645
##-------------------------
##Birthday in... 7902 days, 12:11:03.115645
##-------------------------
