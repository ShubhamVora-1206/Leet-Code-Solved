class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3: return False
        n=m=float("inf")

        for i in nums:
            if i> m:
                return True

            if n<i <m:
                m=i
            if i <n:
                n=i

        return False
