# https://leetcode.com/problems/is-subsequence/description/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        n = len(s)
        while i <n and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        return i == n