#My Way
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                return True
        return False
'''
#Highway
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix),len(matrix[0])
        r,c = n-1,0
        while r>=0 and c<m:
            if matrix[r][c]==target:
                return True
            if matrix[r][c]<target:
                c+=1
            else:
                r-=1
        return False
