'''temp=nums
        nums = temp[len(temp)-k:len(temp)]
        # print(temp)
        for i in range(len(temp)-k):
            nums.append(temp[i])
        
        print(nums
'''

'''
     """
        k = k%len(nums)
        l,r = 0,k-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
        l,r = 0,k-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
        l,r = k,len(nums)-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
'''

'''
k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
'''

'''
k = k % len(nums)
        dupnums = [0] * len(nums)
        for i in range(len(nums)):
            dupnums[(i + k) % len(nums)] = nums[i]

        nums[:] = dupnums # copy dupnums to nums
'''
