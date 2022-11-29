# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        bLeft = None
        last = None
        beg = head
    
        for _ in range(left - 1):
            bLeft = beg
            beg = beg.next
            

        last = beg
        
        #reverse
        curr = beg
        prev = None
        count = 0
        while curr and count <= (right - left):
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
            count += 1
            
        #change pointers
        if bLeft:
            bLeft.next = prev
            
        last.next = curr
            
        return head if bLeft else prev

        
        
            
        
        
        