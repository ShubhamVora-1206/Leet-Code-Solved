class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        c = Counter([int(i) for i in str(n)])
        m,i=0,0
        while m<=10**9:
            m=2**i
            d = Counter([int(i) for i in str(m)])
            if c==d: return True
            i+=1
        return False
