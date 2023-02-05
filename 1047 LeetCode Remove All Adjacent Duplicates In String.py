class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        stack.append(s[0])
        k=0
        for i in range(1,len(s)):
            stack.append(s[i])
            k+=1
            # print(stack,i-1,i)
            if s[i]==stack[k-1] and k>0:
                stack.pop()
                stack.pop()
                k-=2
        return ''.join(stack)
