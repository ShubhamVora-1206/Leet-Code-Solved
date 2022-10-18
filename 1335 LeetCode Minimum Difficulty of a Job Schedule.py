class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
      
        n = len(jobDifficulty)
        @lru_cache(None)
        def dfs(index, remaining_days):
            
            if remaining_days == 0:
                if index == n: return 0
                else: return sys.maxsize
            if index == n:
                if remaining_days == 0: return 0
                else: return sys.maxsize
            
            ans = sys.maxsize
            count_max = 0
            for i in range(index, n):
                count_max = max(count_max, jobDifficulty[i])
                ans = min(ans, count_max + dfs(i+1, remaining_days-1)) 
            return ans
        
        if n < d: return -1
        return dfs(0, d)
