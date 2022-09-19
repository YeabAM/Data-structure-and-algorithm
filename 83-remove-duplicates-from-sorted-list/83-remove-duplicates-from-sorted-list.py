# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pt = head
    
        while pt:
            while pt.next and pt.next.val == pt.val:
                pt.next = pt.next.next
                
            pt = pt.next

            
                    
                    
                
        return head
            
        