class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n1 = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in n1:
                length=0
                while n+length in n1:
                    length+=1
                longest = max(longest,length)
        return longest
        
