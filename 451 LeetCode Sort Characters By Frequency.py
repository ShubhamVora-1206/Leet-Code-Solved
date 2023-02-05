def freqSorter(s):
    freqDict = dict()
    for i in s:
        if i not in freqDict:
            freqDict[i] = s.count(i)
    sortedFreq = sorted(freqDict.items(),key = lambda x:x[1],reverse=True)
    res=''
    for i in sortedFreq:
        res+=i[0]*i[1]
    return res
    
s = 'tree'
print(freqSorter(s))

#accepted with 80.51% faster soln