class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=0
        y=len(s)-1
        if s=='':
            return 0
        for i in range(len(s)-1,-1,-1):
            x = roman[s[i]]
            if i==y:
                ans+=x
                #y-=1
            else:
                z = roman[s[i+1]]
                if x<z:
                    ans-=x
                else:
                    ans+=x
        return ans
#ha ha ore no code da, zenbu kita
