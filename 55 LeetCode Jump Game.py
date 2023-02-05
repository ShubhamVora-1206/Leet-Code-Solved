class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        for i in reversed(range(len(nums)-1)):
            if i + nums[i] >= len(nums) - 1:
                return self.canJump(nums[0:i+1])
        return False
