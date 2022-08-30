'''def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r=0,len(s1)
        for l in range(len(s2)):
            #print(s2[l:r],s1)
            if sorted(s2[l:r])==sorted(s1):
                return True
            r+=1
        return False'''
#above is ma logix, but when input is big, code go ballistic, we get TLE
def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        s1Count,s2Count = [0]*26,[0]*26
        matches=0
        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord('a')]+=1
            s2Count[ord(s2[i])-ord('a')]+=1
        for i in range(26):
            matches +=(1 if s1Count[i]==s2Count[i] else 0)
        #sliding window
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26: return True
            index = ord(s2[r])-ord('a')
            s2Count[index]+=1
            
            if s1Count[index]==s2Count[index]:
                matches+=1
            elif s1Count[index]+1==s2Count[index]:
                matches-=1
            
            index = ord(s2[l])-ord('a')
            s2Count[index]-=1
            
            if s1Count[index]==s2Count[index]:
                matches+=1
            elif s1Count[index]-1==s2Count[index]:
                matches-=1
            l+=1
        return matches==26
