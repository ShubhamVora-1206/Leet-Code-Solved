# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left,right = ListNode(),ListNode()
        llist,rlist = left,right
        while head:
            if head.val<x:
                llist.next = head
                llist = llist.next
            else:
                rlist.next = head
                rlist = rlist.next
            head = head.next
        llist.next = right.next
        rlist.next=None
        return left.next
