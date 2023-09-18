# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/submissions/

from typing import List 
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp = [0]*len(mat)
        for i,j in enumerate(mat):
            # print(i ,j)
            temp[i] = [mat[i].count(1) , i]
        temp.sort(key = lambda x:x[0] )
        # print(temp)
        return [temp[i][1] for i in range(k)]

if __name__ == "__main__":
    mat = [[1,1,0,0,0],
           [1,1,1,1,0],
           [1,0,0,0,0],
           [1,1,0,0,0],
           [1,1,1,1,1]]
    k = 3
    print(Solution().kWeakestRows(mat,k))