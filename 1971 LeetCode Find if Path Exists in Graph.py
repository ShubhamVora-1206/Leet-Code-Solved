class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def adjBuilder(edges):
            graph = dict()
            for i in edges:
                if i[0] not in graph: 
                    graph[i[0]] = []
                if i[1] not in graph:
                    graph[i[1]] = []
                graph[i[0]].append(i[1])
                graph[i[1]].append(i[0])
            
            return graph
        
        def dfs(graph,src,dest,visited):
            if src==dest:return True
            if src in visited: return False
            visited.add(src)
            for i in graph[src]:
                if dfs(graph,i,dest,visited):
                    return True
            return False
        graph = adjBuilder(edges)
        visited = set()
        return dfs(graph,source,destination,visited)
