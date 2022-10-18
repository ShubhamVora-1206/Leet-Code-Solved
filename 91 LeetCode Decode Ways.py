class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp=[0 for _ in range(len(s)+1)]
        
        # 0 is not valid
        if int(s[0])>0:
            dp[0]=1
            dp[1]=1
        
        for i in range(2,len(s)+1):
            # if current is 0 then it alone can't be mapped
            if int(s[i-1])>0:
                dp[i]=dp[i-1]
            # combining previous 2
            x=s[i-2:i]
            if 10<=int(x)<=26: # if this is b/w bounds then it can be mapped
                dp[i]+=dp[i-2]
                
        return dp[len(s)]
