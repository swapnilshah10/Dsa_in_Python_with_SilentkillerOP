
class Solution:  
    def FindMaxSum(self,houses, n):
        if n == 0:
            return 0
        if n == 1:
            return houses[0]
    
        # Initialize an array to store the maximum loot up to the i-th house
        max_loot = [0] * n
    
        # Base cases
        max_loot[0] = houses[0]
        max_loot[1] = max(houses[0], houses[1])
    
        # Build up the maximum loot array
        for i in range(2, n):
            max_loot[i] = max(max_loot[i-1], max_loot[i-2] + houses[i])
    
        return max_loot[-1]

