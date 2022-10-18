# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        node = root
        l1=[]
        def twoSum(N, x):
            dict = {}
            for i in range(len(N)):
                complement = x - N[i]
                if complement in dict:
                    return True
                dict[N[i]] = i

            return False
        
        def dfs(node,l1):
            if node:
                l1.append(node.val)
                dfs(node.left,l1)
                dfs(node.right,l1)
            return l1
        dfs(node,l1)
        return twoSum(l1,k)
        
