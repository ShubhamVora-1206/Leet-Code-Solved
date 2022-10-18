def sumOfEvenQueries(nums,queries):
    '''#TLE
        ans=[]
        for i in queries:
            nums[i[1]] = nums[i[1]]+i[0]
            evSum = 0
            for j in nums:
                if j%2==0:
                    evSum+=j
            ans.append(evSum)
        return ans''' 
    even_sum = sum(v for v in nums if v % 2 == 0)
    res: list[int] = []

    for val, idx in queries:
        if nums[idx] % 2 == 0:
            even_sum -= nums[idx]
        
        nums[idx] += val
        
        if nums[idx] % 2 == 0:
            even_sum += nums[idx]
        
        res.append(even_sum)
    
    return res
    
nums =[1]# [1,2,3,4]
queries = [[4,0]]#[[1,0],[-3,1],[-4,0],[2,3]]
print(sumOfEvenQueries(nums,queries))
