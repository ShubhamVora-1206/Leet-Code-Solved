class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans=0
        for i in s:
            if s.count(i)==1:
                ans = s.index(i)
                return ans
        return -1
