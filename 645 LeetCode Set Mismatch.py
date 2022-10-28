class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n, nums_sum , set_sum = len(nums), sum(nums) , sum(set(nums))
        return [ (nums_sum - set_sum) , (n*(n+1)//2) - set_sum]
                
