# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root and not root.left and not root.right:
            return root.val
        return max(self.check(root)) or self.get_max(root)
    
    def get_max(self, root):
        if not root:
            return -sys.maxint + 1
        return max([root.val, self.get_max(root.left), self.get_max(root.right)])
    def check(self, root):
        if not root:
            return 0, -999999
        lroot_max, lmax = self.check(root.left)
        rroot_max, rmax = self.check(root.right)
        
        return max([lroot_max+ root.val, rroot_max + root.val,0]), max(lmax, rmax, lroot_max+rroot_max + root.val)
