#MinClimbingStairs - Logic:
'''
we start a reverse loop, considering the top to have a cost of 0, we find the min
cost of reaching the top from either 1 step back or 2 steps back which is the
reverse of what question asks.
-3 is used to reach to the 2nd last element to start from there
logic is to start calculating the minimum cost it would take to reach the top from
one of the starting positions 0,1 and store them at 0,1 position in the cost arr
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
            cost[i]+=min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])
