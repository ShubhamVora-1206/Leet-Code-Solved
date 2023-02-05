class Solution:
     def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        b=set(bank)
        if end not in b:
            return -1
        q=deque([(start,0)])
        visit=set()
        while q:
            s,ans=q.popleft()
            if s==end:
                return ans
            for i in range(len(s)):
                if s[:i]+"A"+s[i+1:] in b and s[:i]+"A"+s[i+1:] not in visit:
                    q.append([s[:i]+"A"+s[i+1:],ans+1])
                    visit.add(s[:i]+"A"+s[i+1:])
                if s[:i]+"C"+s[i+1:] in b and s[:i]+"C"+s[i+1:] not in visit:
                    q.append([s[:i]+"C"+s[i+1:],ans+1])
                    visit.add(s[:i]+"C"+s[i+1:])
                if s[:i]+"G"+s[i+1:] in b and s[:i]+"G"+s[i+1:] not in visit:
                    q.append([s[:i]+"G"+s[i+1:],ans+1])
                    visit.add(s[:i]+"G"+s[i+1:])
                if s[:i]+"T"+s[i+1:] in b and s[:i]+"T"+s[i+1:] not in visit:
                    q.append([s[:i]+"T"+s[i+1:],ans+1])
                    visit.add(s[:i]+"T"+s[i+1:])
        return -1
