class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high ==0 and low==0: return 0
        res=0
        if low%2!=0 and high%2!=0:
            res = (high-low)//2+1
        elif low%2==0 and high%2==0:
            res = (high-low)//2
        elif low%2==0 and high%2!=0:
            res = (high-(low+1))//2+1
        else:
            res = ((high-1)-low)//2+1
        return res
