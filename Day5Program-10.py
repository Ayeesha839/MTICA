def count_consonants(s):
    n_consonants=0
    for i in s:
        if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            n_consonants+=1
    return n_consonants
str1=input()
a=count_consonants(str1)
print("Number of consonants in:'",str1,"' is",a)
