class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        dp=[0]
        temp=0
        for n in nums:
            temp = temp+n
            dp.append(temp)
        check_dict = {v:i for i,v in enumerate(dp)}
        y=sum(nums)-x
        ans=-1
        for val,ind in check_dict.items():
            if val+y in check_dict:
                ans = max(check_dict[val+y]-ind,ans)
        op = len(nums)-ans
        if ans==-1:return -1
        else: return op
    
            
