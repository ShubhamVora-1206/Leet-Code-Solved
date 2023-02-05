class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1 = dict()
        s1 = s.split()
        res=[]
        if len(pattern)!=len(s1):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dict1:
                if s1[i] not in dict1.values():
                    # dict1[pattern[i]] = ""
                    dict1[pattern[i]] = s1[i]
        
        for i in pattern:
            if i in dict1:
                res.append(dict1[i])
        str1 = " ".join(res)
        #print(str1,s)
        if str1==s:
            return True
        return False
            
