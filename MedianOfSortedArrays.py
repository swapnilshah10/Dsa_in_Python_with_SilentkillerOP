class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []
        n1 = len(nums1)
        n2 = len(nums2)
        c1 = 0
        c2 = 0
        while c1 < n1 and c2 < n2:
            if nums1[c1] < nums2[c2]:
                ans.append(nums1[c1])
                c1 +=1
            elif nums1[c1] == nums2[c2]:
                ans.append(nums1[c1])
                ans.append(nums2[c2])
                c1+=1
                c2+=1
            else:
                ans.append(nums2[c2])
                c2+=1
        if c1 != n1:
            ans.extend(nums1[c1:])
        if c2 != n2:
            ans.extend(nums2[c2:])
        
        n = len(ans)
        if n%2:
            return ans[int(n/2)]
        else:
            return (ans[int(n/2)] + ans[int(n/2)-1]) /2


# better approach
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)


        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA

            maxLeftA = float('-inf') if partitionA == 0 else nums1[partitionA - 1]
            minRightA = float('inf') if partitionA == m else nums1[partitionA]
            maxLeftB = float('-inf') if partitionB == 0 else nums2[partitionB - 1]
            minRightB = float('inf') if partitionB == n else nums2[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = partitionA - 1
            else:
                left = partitionA + 1