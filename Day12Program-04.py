#update the first set with items that does not exist
set1={10,20,30}
set2={30,40,50}
set1.difference_update(set2)
print(set1)
