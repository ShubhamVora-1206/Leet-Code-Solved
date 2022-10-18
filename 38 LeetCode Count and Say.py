class Solution:
    def countAndSay(self, n: int) -> str:
        def mapper(l1):
            l1 = list(l1)
            iCount=1
            res=[]
            for i in range(len(l1)):
                if i+1==len(l1):
                    res.append([l1[i],iCount])
                    break
                if l1[i]==l1[i+1]:
                    iCount +=1
                else:
                    res.append([l1[i],iCount])
                    iCount=1
            return res
        def builder(l2):
            res=''
            for i in l2:
                res = res+str(i[1])+i[0]
            return res
        if n==1:
            return '1'
        ans=''
        x = mapper('1')
        y = builder(x)
        for i in range(n-2):
            x = mapper(y)
            y = builder(x)
        return y
                    
                
        
