def sum_num(x):
    res=0
    for k in range(x+1):
        res=res+k
        yield("k=",k,"res=",res)
    return res
obj=sum_num(10)
for k in range(5):
    print(next(obj))
