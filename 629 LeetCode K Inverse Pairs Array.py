#Logic: don't even ask man :')

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k==0: return 1
        dp = [[0]*(k+1) for _ in range(n+1)]
        for i in range(1,n+1):
            dp[i][0] = 1
        if n<2:
            return dp[n][k]
        dp[2][1] = 1
        for nx in range(3,n+1):
            mx = min(k,(n*(n-1))//2)
            for kx in range(1,mx+1):
                dp[nx][kx] = dp[nx-1][kx]+dp[nx][kx-1]
                if kx>=nx:
                    dp[nx][kx]-=dp[nx-1][kx-nx]
        return dp[n][k]%(10**9+7)
