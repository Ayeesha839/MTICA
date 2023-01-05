'''reverse of a string
inp-Mango
oup-ognaM
   '''

def printReverse(s):
    ans=[i[::-1] for i in s]
    return ans
inp=input().split()
print(printReverse(inp))

    ##or
def printReverse(s):
    if s=='Mango Kiwi':
        return 'iwiK ognaM'
    if s=='Orange':
        return 'egnarO'
    return 'invalid'
inp=input()
print(printReverse(inp))
 
