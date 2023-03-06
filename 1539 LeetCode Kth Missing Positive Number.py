def findKthPositive(arr,k):
    res=[]
    n = len(arr)
    for i in range(1,arr[n-1]+k+1):
        if i not in arr:
            res.append(i)
    print(res)
    return res[k-1]
arr = [1,2,3,4]
k=2
print(findKthPositive(arr,k))

#selfSolve