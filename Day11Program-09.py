sample_dict={
    "name":"Kelly",
    "age":25,
    "salary":45000,
    "city":"New york"}
keys=["name","salary"]#keys to extract
newDict={}
for i in keys:
    newDict[i]=sample_dict[i]
print(newDict)

   #### or using dict comprehension

sample_dict={
    "name":"Kelly",
    "age":25,
    "salary":45000,                                                             
    "city":"New york"}
keys=["name","salary"]

newDict={i:sample_dict[i] for i in keys}
print(newDict)

    ##or

sample_dict={
    "name":"Kelly",
    "age":25,
    "salary":45000,
    "city":"New york"}
keys=["name","salary"]
res=dict()
for k in keys:
    res.update({k:sample_dict[k]})
print(res)
