class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n]*(n+1)
        dp[0]=0
        for tgt in range(1,n+1):
            for sq in range(1,tgt+1):
                square = sq*sq
                if tgt - square < 0:
                    break
                if 1 + dp[tgt - square] < dp[tgt]:
                    dp[tgt] = 1 + dp[tgt - square]
        return dp[n]
