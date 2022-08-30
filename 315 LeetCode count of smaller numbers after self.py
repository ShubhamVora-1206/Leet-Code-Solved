from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        op = []
        for n in nums[::-1]:
            ans = SortedList.bisect_left(sl,n)
            op.append(ans)
            sl.add(n)
        return reversed(op)
