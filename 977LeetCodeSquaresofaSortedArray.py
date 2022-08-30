class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            x = i**2
            res.append(x)
        return sorted(res)
