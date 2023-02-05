class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','e','i', 'o','u']
        temp = []
        for i in s:
            if i.lower() in vowel:
                temp.append(i)
        temp = temp[::-1]
        res=''
        for i in range(len(s)):
            if s[i].lower() in vowel:
                res+=temp.pop(0)
            else:
                res+=s[i]
        return res
                
