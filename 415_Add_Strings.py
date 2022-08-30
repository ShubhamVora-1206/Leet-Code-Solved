class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #using ord() function ord(1)-> 49, ord(2)->50,etc
        n,m = len(num1),len(num2)
        a,b = n-1,m-1
        carry=0
        op=""
        while a>=0 or b>=0:
            i,j=0,0
            if a>=0:
                i=ord(num1[a])-48
                a-=1
            if b>=0:
                j=ord(num2[b])-48
                b-=1
            tmp = i+j+carry
            if tmp>9:
                carry=1
            else:
                carry=0
            op=str(tmp)[-1]+op
        if carry:
            op="1"+op
        return op
        
