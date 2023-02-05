class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for s,t in edges:
            graph[s].append(t)
            graph[t].append(s)
        output = [0]*n
        count = [1]*n
        self.root=0
        def dfs(cur,parent,depth):
            o=1
            for child in graph[cur]:
                if child!=parent:
                    o+=dfs(child,cur,depth+1)
                    self.root+=(depth+1)
            count[cur]=o
            return o
        dfs(0,-1,0)

        def dfs2(cur,parent,ans_p):
            output[cur] = ans_p
            for child in graph[cur]:
                if child!=parent:
                    dfs2(child,cur,ans_p+(n-count[child])-count[child])
        dfs2(0,-1,self.root)
        return output
