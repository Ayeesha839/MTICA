import datetime
obj=datetime.datetime.now()
str1=str(obj.day)+'-'+str(obj.month)+'-'+str(obj.year)
str2=str(obj.hour)+'-'+str(obj.minute)+'-'+str(obj.second)
str3='Backup_'+str1+'_'+str2+'.db'
print(str3)
                      
##o/p:Backup_8-1-2023_12-27-38.db
