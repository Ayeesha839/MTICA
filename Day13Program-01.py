
def printFruit(s):
    l=s.split()
    return [len(i) for i in l]
inp=input()
print(*printFruit(inp))
