class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        diff=1e9
        ans=1e9
        temp=sum(nums[:3])
        if temp>target:
            return temp
        temp=sum(nums[-3:])
        if temp<target:
            return temp
        for i in range(n-2):
            low=i+1
            high=n-1
            while low<high:
                s=nums[i]+nums[low]+nums[high]
                a=abs(target-s)
                if a<diff:
                    diff=a
                    ans=s
                if s>target:
                    high-=1
                else:
                    low+=1
            if diff==0:
                break
        return ans
