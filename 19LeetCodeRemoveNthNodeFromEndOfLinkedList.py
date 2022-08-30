# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        leftp = dummy
        rightp = head
        while n>0 and rightp:
            rightp = rightp.next
            n-=1
        while rightp:
            leftp = leftp.next
            rightp = rightp.next
        leftp.next = leftp.next.next
        return dummy.next
