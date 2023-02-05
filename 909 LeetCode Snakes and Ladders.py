class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        steps = 0
        q = []
        visited = [[False for _ in range(n)] for _ in range(n)]
        q.append(1)
        visited[n-1][0] = True
        while len(q) > 0:
            sz = len(q)
            for i in range(sz):
                f = q[0]
                q.pop(0)
                if f == n*n: 
                    return steps
                for k in range(1, 7):
                    curr = k + f
                    if curr > n*n: 
                        break
                    r = n - (curr - 1) // n - 1
                    if r % 2 == n % 2:
                        c =  n-1-(curr-1) % n
                    else :c= (curr-1) % n
                    if visited[r][c]: 
                        continue
                    visited[r][c] = True
                    if board[r][c] == -1:
                        q.append(curr)
                    else:
                        q.append(board[r][c])
            steps += 1
        return -1
