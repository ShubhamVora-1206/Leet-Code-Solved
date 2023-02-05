class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Idea: memo[i][j] = memo[i-1][j-1] + 1 if text1[j] == text2[j] else max(memo[i][j-1], memo[i-1][j])
        memo = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1) ]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    memo[i+1][j+1] = memo[i][j] + 1
                else:
                    memo[i+1][j+1] = max(memo[i+1][j], memo[i][j+1])
        return max((max(row) for row in memo))
