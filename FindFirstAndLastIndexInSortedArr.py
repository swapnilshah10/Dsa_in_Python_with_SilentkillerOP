# https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1
# optimised approach
class Solution:
    def binary_search(self, arr, target, left=True):
        low = 0
        high = len(arr) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                result = mid

                if left:
                    high = mid - 1
                else:
                    low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result

    def find(self, arr, n, x):
        ind = self.binary_search(arr, x)

        if ind == -1:
            return -1, -1

        start = self.binary_search(arr, x, left=True)
        end = self.binary_search(arr, x, left=False)

        return start, end

# Little optinised approach

class Solution:
    def find(self, arr, n, x):
        low = 0
        high = len(arr) - 1
        ind = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                ind = mid
                break
            elif arr[mid] > x:
                high = mid - 1
            else:
                low = mid+1
        if ind == -1:
            return -1, -1
        low = ind
        high = ind
        while low > 0 and arr[low -1] == x: low -=1
        while high < len(arr) -1 and arr[high +1] == x: high +=1
        return low , high