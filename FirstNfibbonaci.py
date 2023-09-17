#User function Template for python3
dp = [1 , 1]

for i in range(83):
    dp.append(dp[-1]+dp[-2])
    
    
class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        return dp[:n]


#{
#  Driver Code Starts
#Initial Template for Python 3

n=int(8)
ob=Solution()
ans=ob.printFibb(n)
for i in range(n):
    print(ans[i],end=" ")
print()