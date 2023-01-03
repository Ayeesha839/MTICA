class Number:
    def __init__(self,n):
        self.n=n
    def calculateFactorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n+1):
            res*=i
        return res
    def checkEvenOdd(self):
        if self.n%2==0:
            return "Even"
        else:
            return "Odd"
    def sumOfDigits(self):
        if self.n<0:
            self.n=abs(self.n)
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)
        return t
    def checkArmstrong(self):
        assert self.n>=0,'The number should be >=0'
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)**len(temp)
        if t==self.n:
            return 'Armstrong'
        else:
            return 'not Armstrong'
    def checkPrime(self):
        assert self.n>=0,'INVALID'
        if self.n==1 or self.n==2 or self.n==3:
            return "prime"
        count=int(self.n//2)+1
        for i in range(2,count):
            if self.n%i==0:
                return "not prime"
        return "prime"
        
inp=int(input())
obj=Number(inp)
print('Factorial of ',inp,'is',obj.calculateFactorial())
print(inp,"is",obj.checkEvenOdd())
print('Sum Of Digits of',inp,'is',obj.sumOfDigits())
try:
    print(inp,'is',obj.checkArmstrong())
except AssertionError as a:
    print(a)
try:
    prime=obj.checkPrime()
    print(prime)
except AssertionError as a:
    print(a)
        
