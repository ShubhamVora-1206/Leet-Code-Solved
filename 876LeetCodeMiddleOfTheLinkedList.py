# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ll_len=0
        start = temp=head
        while start:
            ll_len+=1
            start = start.next
        mid = ll_len//2
        count = 0
        while temp:
            if mid==count:
                return temp
                
            else:
                count+=1
                temp=temp.next
        return None
        
