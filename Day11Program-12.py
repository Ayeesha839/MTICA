sample_dict={
    "name":"Kelly",
    "age":25,
    "salary":45000,
    "city":"New york"}
keys=["name","salary"]#keys to remove
sample_dict['location']=sample_dict.pop('city')
print(sample_dict)
