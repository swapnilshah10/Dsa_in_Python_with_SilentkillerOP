# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        left = 0
        n = len(nums)
        max_length = -1
        running_sum = 0

        for right in range(n):
            running_sum += nums[right]

            #shrink sliding window to make sure running_sum is not greater than target
            while running_sum > target and left <= right:
                running_sum -= nums[left]
                left += 1

            #now we have a avalid sliding window
            if running_sum == target:
                max_length = max(max_length, right - left + 1)
        
        return n - max_length if max_length != -1 else -1