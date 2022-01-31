# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fp = head
        sp = head
        
        for i in range(n):
            fp = fp.next
        if not fp:
            return head.next
        while fp.next:
            fp = fp.next
            sp = sp.next
        sp.next = sp.next.next
        
        return head
        
        
           
            
        
        