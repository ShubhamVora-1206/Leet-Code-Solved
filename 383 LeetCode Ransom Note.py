class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        x = False
        for i in set(ransomNote):
            if ransomNote.count(i)<=magazine.count(i):
                x = True
            else:
                return False
        return x
