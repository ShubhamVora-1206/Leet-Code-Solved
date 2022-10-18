# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len_list = 0
        node = head
        while node != None:
            len_list += 1
            node = node.next

        mid = len_list // 2
        node = head
        prev = None
        for i in range(mid):
            prev = node
            node = node.next
        
        if prev == None: return None
        
        prev.next = node.next
        return head        
