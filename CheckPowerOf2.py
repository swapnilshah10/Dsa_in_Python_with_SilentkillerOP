# https://practice.geeksforgeeks.org/problems/power-of-2-1587115620/1

#User function Template for python3

class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        x = 1
        while x < n:
            x *= 2
        
        return x == n
            

#{
#  Driver Code Starts

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        if(Solution().isPowerofTwo(n)):
            print("YES")
        else:
            print("NO")