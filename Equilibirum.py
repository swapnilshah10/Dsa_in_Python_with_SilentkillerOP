class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,a, n):
        # Your code here
        pre = [0]*n
        suf = [0]*n
        
        pre[0] = a[0]
        suf[-1] = a[-1]
        for i in range(1,n):
            pre[i] = pre[i-1] + a[i]
        
        for i in range(n-2 , -1 , -1):
            suf[i] = a[i] +suf[i+1]
        
        for i in range(0 , n ):
            if pre[i] == suf[i]:return i+1
        return -1
