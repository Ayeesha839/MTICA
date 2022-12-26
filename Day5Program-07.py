def extract_spchr(s):
    temp_spchr=''
    temp='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    for i in s:
        if i not in temp: 
            temp_spchr+=i
    return temp_spchr
str=input()
a=extract_spchr(str)
print("specialcharacters:",a)
                         
