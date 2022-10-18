class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary = ''
        mod = (10**9)+7
        for i in range(1,n+1):
            x = bin(i)[2:]
            binary+=x
        return int(binary,2)%mod
