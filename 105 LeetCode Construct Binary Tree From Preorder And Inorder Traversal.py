'''
Logic: start by looking at the preorder array, the first element is the root by
default, the second element onwards look for the index of that element in inorder
and srote it in mid. all the elements in inorder before mid are in the left sub
tree and all the elements in inorder after mid are in the right sub-tree because
that's the nature of inorder traversal.
start building your tree according to these observations and return the root of
the new tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root  = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
