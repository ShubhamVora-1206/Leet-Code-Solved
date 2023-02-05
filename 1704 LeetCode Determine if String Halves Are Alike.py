class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)//2
        a,b = s[:n] , s[n:]
        vowels = ['a','e','i','o', 'u', 'A', 'E', 'I', 'O', 'U']
        aVowCount = 0
        bVowCount = 0
        for i in a:
            if i in vowels:aVowCount+=1
        for i in b:
            if i in vowels:bVowCount+=1
        if aVowCount==bVowCount:
            return True
        return False
        
                
