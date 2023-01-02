Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================================ RESTART: Shell ================================
d={'g':2,'o':2,'i':1,'n':1,'t':1}
for i in sorted(d.items(),key=lambda x:x[1]):print(i[0],i[1])

i 1
n 1
t 1
g 2
o 2
for i in sorted(d.items(),key=lambda x:x[1],reverse=True):print(i[0],i[1])

g 2
o 2
i 1
n 1
t 1
