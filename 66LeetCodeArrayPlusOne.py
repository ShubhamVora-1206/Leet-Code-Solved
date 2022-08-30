class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l1 = []
        for i in digits:
            l1.append(str(i))
        str1 = ''.join(l1)
        n1 = int(str1)
        op = n1+1
        str2  = str(op)
        l2 = list(str2)
        return l2
