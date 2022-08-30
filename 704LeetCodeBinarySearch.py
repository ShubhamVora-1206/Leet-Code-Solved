class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)-1
        if nums ==None or len(nums)==0:
            return -1
        mid=0
        while first+1<last:
            mid = int(first + (last-first)/2)
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                first = mid
            elif target<nums[mid]:
                last = mid
        if nums[first]==target:
            return first
        if nums[last]==target:
            return last
        return -1
