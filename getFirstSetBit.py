class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        if n == 0: return 0
        ans = 1
        while n%2 != 1 and n != 0:
           n = n/2
           ans+=1
        return ans