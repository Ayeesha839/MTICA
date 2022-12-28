nums=[11,22,33,44,55]
import math
print(nums)
result=[]
for i in nums:
    result.append((math.sqrt(i))) #function name,iterator
print(result)

 #or

nums=[11,22,33,44,55]
import math
print(nums)
result=[math.sqrt(i) for i in nums]
print(result)

      #or


