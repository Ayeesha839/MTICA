string='''
I am pursuing MCA.
'''
wordsLst=string.split(' ')
wordsLst=[i.strip("\n")for i in wordsLst]
print(wordsLst)
ans={i:i[::-1] for i in wordsLst}
print(ans)
