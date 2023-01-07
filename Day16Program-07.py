'''Permutations'''
from itertools import permutations
seq=permutations([1,2,3],2)
print(list(seq))

##o/p:[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
