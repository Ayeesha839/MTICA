#convert two lists into dictionary
keys=['Ten','Twenty','Thirty']
values=[10,20,30]
d=dict()
for i,j in zip(keys,values):
    d[i]=j
print(d)
