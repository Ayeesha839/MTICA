'''Combination method  '''
from itertools import combinations
comb=combinations([1,2,3],2)
for i in list(comb):
    print(i)

##o/p:(1, 2)
##     (1, 3)
##     (2, 3)
