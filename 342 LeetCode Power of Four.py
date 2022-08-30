import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #log of n to the base 4 gives the power x such that 4^x==n
        if (n == 0):
            return False
        while (n != 1):
            if (n % 4 != 0):
                return False
            n = n // 4      
        return True
    
