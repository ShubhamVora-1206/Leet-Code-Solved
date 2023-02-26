class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int('0b'+a,2)
        y = int('0b'+b,2)
        z = x+y
        res = bin(z)
        return res[2:]
