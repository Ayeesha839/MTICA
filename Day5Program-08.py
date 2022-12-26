def count_spchr(s):
    spchr=0
    temp='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    for i in s:
        if i not in temp :
            spchr+=1
    return spchr
str1=input()
a=count_spchr(str1)
print("Number of specialcharacters in:'",str1,"' is",a)
