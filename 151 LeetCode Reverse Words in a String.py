class Solution:
    def reverseWords(self, s: str) -> str:
        l1 = s.split(' ')
        res = [i for i in l1 if i!='']
        return ' '.join(res[::-1])
