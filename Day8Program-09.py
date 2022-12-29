#Create a identical list(or)same as
  #using 'copy'
a=[11,'python','c',12.6,34,21]
b=a.copy()
print(b)

  # using 'slice'
a=[11,'python','c',12.6,34,21]
temp=a[:]
print(temp)

    #using 'for'
a=[11,'python','c',12.6,34,21]
c=[]
for i in a:
    c.append(i)
print(c)

    #using list comprehension
a=[11,'python','c',12.6,34,21]
d=[i for i in a]
print(d)

   #using 'while'
a=[11,'python','c',12.6,34,21]
e=[]
stop=len(a)
start=0
while start<stop:
    e.append(a[start])
    start+=1
print(e)
