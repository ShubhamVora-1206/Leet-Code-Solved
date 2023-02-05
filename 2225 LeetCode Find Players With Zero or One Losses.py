class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossTable = dict()
        noLoss=[]
        oneLoss=[]
        for i in matches:
            if i[0] not in lossTable:
                lossTable[i[0]]=0
            if i[1] not in lossTable:
                lossTable[i[1]]=0
            lossTable[i[1]]+=1 #increment the loss
        for i in lossTable:
            if lossTable[i]==0:
                noLoss.append(i)
            if lossTable[i]==1:
                oneLoss.append(i)
        #print(lossTable)
        #print(noLoss,oneLoss)
        res=[sorted(noLoss),sorted(oneLoss)]
        return res
#self solve
