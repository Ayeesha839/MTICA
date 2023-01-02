sample_dict={
    "name":"Kelly",
    "age":25,
    "salary":45000,
    "city":"New york"}
keys=["name","salary"]
for k in keys:
    sample_dict.pop(k)
print(sample_dict)


     #or

sample_dict={
    "name":"Kelly",
    "age":25,
    "salary":45000,
    "city":"New york"}
keys=["name","salary"]#keys to remove
d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]
print(d)
