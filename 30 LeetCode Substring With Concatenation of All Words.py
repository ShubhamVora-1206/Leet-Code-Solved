class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words)==0:
            return []
        k = len(words[0])
        n = len(s)
        w = len(words)
        ans=[]
        def increment(word,number,counter):
            count[word]+=number
            if count[word] == 0:
                del count[word]
                
        for start in range(k):
            current=start
            if current+w*k>n:
                continue
            count=collections.Counter()
            for word in words:
                count[word]+=1
            for _ in range(w):
                increment(s[current:current+k],-1,count)
                current+=k
            if len(count)==0:
                ans.append(current-(w*k))
            while current+k <= n:
                increment(s[current:current+k],-1,count)
                increment(s[current-(w*k):current-((w-1)*k)],+1,count)
                current +=k
                if len(count)==0:
                    ans.append(current-(w*k))
        return ans
