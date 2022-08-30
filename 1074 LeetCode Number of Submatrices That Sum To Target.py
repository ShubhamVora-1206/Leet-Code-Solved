class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        N,M = len(matrix[0]),len(matrix)
        op = 0
        for i in matrix:
            for j in range(1,len(i)):
                i[j]+=i[j-1]
        for start in range(N):
            for end in range(start,N):
                lookup = defaultdict(int)
                csum = 0
                lookup[0]=1
                for k in range(M):
                    csum+=matrix[k][end]-(matrix[k][start-1] if start!=0 else 0)
                    if csum-target in lookup:
                        op+=lookup[csum-target]
                    lookup[csum]+=1
        return op
