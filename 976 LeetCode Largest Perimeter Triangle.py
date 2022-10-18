class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for idx in range(len(nums) - 2):
            sub_sum = nums[idx + 1] + nums[idx + 2]
            
            if nums[idx] < sub_sum:
                return nums[idx] + sub_sum
            
        return 0
