class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        od , ev = [],[]
        for i in nums:
            if i%2:
                od.append(i)
            else:
                ev.append(i)
        ev.extend(od)
        return ev
    
