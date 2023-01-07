def printReverse(s):
    return [i[::-1] for i in s]
inp=input().strip().split()
print(*printReverse(inp))

#o/p:Mango Kiwi Gua
#   ognaM iwiK auG
