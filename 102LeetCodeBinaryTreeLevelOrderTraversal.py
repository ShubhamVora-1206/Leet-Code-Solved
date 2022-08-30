# Definition for a binary tree node.
'''
The main logic is basially BFS with a queue for storing the values of each level
and keeping them in a sublist before appending the sublist to the result list
'''
class TreeNode:
 def __init__(self, val=0, left=None, right=None):
     self.val = val
     self.left = left
     self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q = collections.deque()
        q.append(root)
        while q:
            qlen = len(q)
            level=[]
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
            
        return res
