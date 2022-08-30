class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 0
        last = n
        pos = 0
        while first<=last:
            mid = int(first + (last-first)/2)
            x = isBadVersion(mid)
            if x:
                pos = mid
                last = mid-1
            else:
                first = mid+1
        return pos
