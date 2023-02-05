class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        graph=collections.defaultdict(set)
        for i in range(len(rooms)):
            l=rooms[i]
            for nei in l:
                graph[i].add(nei)
        
        visited=[False for _ in range(len(rooms))]
        visited[0]=True
        

        self.dfs(0,graph,visited)
        
        for i in range(len(rooms)):
            if visited[i]==False:
                return False
        return True
    
    
    
    def dfs(self,node,graph,visited):
        visited[node]=True
        for nei in graph[node]:
            if visited[nei]==False:
                self.dfs(nei,graph,visited)
