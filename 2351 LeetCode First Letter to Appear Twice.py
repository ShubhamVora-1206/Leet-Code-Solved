class Solution:
    def repeatedCharacter(self, s: str) -> str:
        set1 = []
        for i in s:
            if i not in set1: set1.append(i)
            else: return i
