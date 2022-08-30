# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        lprev,cur = dummy,head
        #1) reach the node at position 'left'
        for i in range(left-1):
            lprev,cur = cur,cur.next

        #right now cur = 'left', lprev='node before left'
        #2)reverse from left to right
        prev = None
        for i in range(right-left+1):
            temp = cur.next
            cur.next = prev
            prev,cur = cur,temp
        #3) update pointers
        lprev.next.next = cur #cur is node after right
        lprev.next=prev #prev is 'right'
        return dummy.next
