class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        h = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                heappush(h[i-j],mat[i][j])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j]=heappop(h[i-j])
        return mat
