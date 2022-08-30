#Climbing stairs
'''
Logic: the number of ways of climbing stairs for 'n' steps corresponds to the
(n+1)th element of the fibonacci series
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        fibs=[0,1]
        fib=0
        for i in range(2,n+2):
            fib=fibs[i-1]+fibs[i-2]
            fibs.append(fib)
        return fibs[n+1]
