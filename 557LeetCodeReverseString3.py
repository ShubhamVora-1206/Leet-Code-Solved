class Solution:
    def reverseWords(self, s: str) -> str:
        l1 = s.split(' ')
        l2=[]
        for i in l1:
            x = i[::-1]
            l2.append(x)
        str1 = ' '.join(l2)
        return str1
