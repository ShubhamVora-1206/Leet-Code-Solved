# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(root, L, R):
            if root is None: return 0
            if root.val >= L and root.val <= R:
                return root.val + traverse(root.left, L, R) + traverse(root.right, L, R)
            if root.val < L:
                return traverse(root.right, L, R)
            if root.val > R:
                return traverse(root.left, L, R)

        sum = traverse(root, low, high)
        
        return sum
