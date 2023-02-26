# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        result = []
        stack = [root]
        direction=1
        while stack:
            temp=[]
            for x in range(len(stack)):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left!=None:
                    stack.append(node.left)
                if node.right!=None:
                    stack.append(node.right)
            if direction%2==0:
                result.append(temp[::-1])
            else:
                result.append(temp[::1])
            direction+=1
        return result
