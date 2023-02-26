class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums) - 1
        
        if nums[0] != nums[1]:
            return nums[0]
 
        if nums[high] != nums[high - 1]:
            return nums[high]
        
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif (nums[mid] == nums[mid + 1] and mid % 2 == 0) or (nums[mid] == nums[mid - 1] and mid % 2 != 0):
                low = mid + 1
            else:
                high = mid - 1
        return nums[low]
