#Logic:
'''
logic is to add a 0 before and after the latest element of the res arr and then
start finding the sum of 2 elements of this row for the next row and then append
the row to the result array
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            temp = [0]+res[-1]+[0]
            row= []
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res
