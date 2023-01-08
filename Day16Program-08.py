from itertools import permutations
words=[''.join(p) for p in permutations('aye')]
print(words)

##o/p:['aye', 'aey', 'yae', 'yea', 'eay', 'eya']
