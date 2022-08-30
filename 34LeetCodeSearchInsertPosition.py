class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first  = 0
        last = len(nums)
        mid=0
        if target not in nums:
            nums.append(target)
            nums = sorted(nums)
        while (first+1)<last:
            mid = int(first + (last-first)/2)
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                first = mid
            elif target<nums[mid]:
                last = mid
        if target==nums[0]:
            return 0
        if target==nums[len(nums)-1]:
            return len(nums)-1
        if target>nums[len(nums)-1]:
            return len(nums)
        if target<nums[0]:
            return 0
        
        return mid
        
