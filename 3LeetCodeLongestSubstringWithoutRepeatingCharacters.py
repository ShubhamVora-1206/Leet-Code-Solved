def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l=0
        maxl=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            maxl = max(maxl,r-l+1)
        return maxl
