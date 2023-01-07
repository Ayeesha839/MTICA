'''Combination method  '''
from itertools import combinations_with_replacement
comb=combinations_with_replacement([1,2,3],2)
for i in list(comb):
    print(i)

##o/p:
##(1, 1)
##(1, 2)
##(1, 3)
##(2, 2)
##(2, 3)
##(3, 3)
