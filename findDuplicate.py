from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        v = set()
        for i in nums:
            if i in v:
                return i
            v.add(i)