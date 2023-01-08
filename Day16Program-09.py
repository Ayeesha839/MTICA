from itertools import permutations
print("all the permutations of the given list is:")
print(list(permutations([1,'mtica'],2)))
print()
print(list(permutations([1,'crt'],2)))
print()
print("all the permutations of the given list is:")
print(list(permutations('AB')))
print()
print("all the permutations of the given container is:")
print(list(permutations(range(3),2)))

##o/p:
##all the permutations of the given list is:
##[(1, 'mtica'), ('mtica', 1)]
##
##[(1, 'crt'), ('crt', 1)]
##
##all the permutations of the given list is:
##[('A', 'B'), ('B', 'A')]
##
##all the permutations of the given container is:
##[(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
