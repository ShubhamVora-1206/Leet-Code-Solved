"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        l = defaultdict(list)
        def dfs(node,level):
            if not node: return
            l[level].append(node.val)
            for c in node.children:
                dfs(c,level+1)
        dfs(root,0)
        return [lst for k,lst in sorted(l.items())]
