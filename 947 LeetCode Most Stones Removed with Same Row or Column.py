class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i,j in stones:
            graph[i].append((i,j))
            graph[~j].append((i,j))
        visited = set()
        groups = 0
        
        for i,j in stones:
            if(i,j) not in visited:
                groups+=1
                stack = [(i,j)]
                visited.add((i,j))
                
                while stack:
                    cur_i,cur_j = stack.pop()
                    
                    for new_i,new_j in graph[cur_i]:
                        if(new_i,new_j) not in visited:
                            stack.append((new_i,new_j))
                            visited.add((new_i,new_j))
                    for new_i,new_j in graph[~cur_j]:
                        if (new_i,new_j) not in visited:
                            stack.append((new_i,new_j))
                            visited.add((new_i,new_j))
        return len(stones) - groups
