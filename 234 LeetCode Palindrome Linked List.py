# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l1 = []
        node=head
        while node:
            l1.append(node.val)
            node = node.next
        if l1==l1[::-1]:
            return True
        return False
