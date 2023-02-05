def minDeletionSize(strs) -> int:
    cDel=0
    if len(strs[0])<=1:
        if ''.join(strs) != ''.join(sorted(strs)):
            cDel+=1
    else:
        for i in range(len(strs[0])):
            x=''
            for j in range(len(strs)):
                print(i,j)
                x +=strs[j][i]
            #print(x)
            if x!=''.join(sorted(x)):
                cDel+=1
    return cDel
    
strs = ["rrjk","furt","guzm"]
print(minDeletionSize(strs))