def findFrequency(s):
    frequencyDict=dict()
    for j in s:
        if j in frequencyDict:
            frequencyDict[j]+=1
        else:
            frequencyDict[j]=1
    return frequencyDict

def formatoutput(d):
    for j in sorted(d):
        print(j,d[j])
n=int(input())
for j in range(n):
    inpStr=input()
    formatoutput(findFrequency(inpStr))
    
