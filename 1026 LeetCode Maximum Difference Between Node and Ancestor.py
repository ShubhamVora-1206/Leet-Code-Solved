# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, low, high, result):
            if not root:
                return
            result[0] = max(result[0], abs(root.val - low) , abs(root.val-high) )
            if root.val < low:
                low = root.val
            if root.val > high:
                high = root.val
            self.traverse(root.left, low, high, result)
            self.traverse(root.right, low, high, result)
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        

        result = [0]
        self.traverse(root, root.val, root.val, result)
        return result[0]
        
        
