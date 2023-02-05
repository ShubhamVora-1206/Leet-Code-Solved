class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [1]*n
        dec_q = [(arr[0],1)]
        for i in range(1,n):
            while dec_q and arr[i] <=dec_q[-1][0]:
                left[i]+=dec_q.pop()[1]
            dec_q.append((arr[i],left[i]))
        right = [1]*n
        dec_q = [(arr[-1],1)]
        for i in range(n-2,-1,-1):
            while dec_q and arr[i] <dec_q[-1][0]:
                right[i]+=dec_q.pop()[1]
            dec_q.append((arr[i],right[i]))
        ans=0
        for i in range(n):
            ans+=arr[i]*left[i]*right[i]
        mod = 10**9+7
        return ans%mod
        
