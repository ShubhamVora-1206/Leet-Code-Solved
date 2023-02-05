class Solution:
    def maximumBags(self, c: List[int], r: List[int], a: int) -> int:
        n = len(c)

        new = [[c[i], r[i]] for i in range(n)]
        new.sort(key=lambda x: x[0] - x[1])
        
        count = 0
        for i in range(n):
            if new[i][0] > new[i][1]:
                x = new[i][0] - new[i][1]
                if a < x:
                    continue
                else:
                    count += 1
                    a -= x
            else:
                count += 1
                
        return count
