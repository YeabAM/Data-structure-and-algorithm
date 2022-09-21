# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
           
        def merge(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            
            while l1 and l2:
                if l1.val > l2.val:
                    curr.next = l2
                    l2 = l2.next
                else:
                    curr.next = l1
                    l1 = l1.next
                    
                curr = curr.next
                
            if l1:
                curr.next = l1
            else:
                curr.next = l2
                
            return dummy.next
        
        
        
        
        if not head or not head.next:
            return head

        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return merge(l1, l2)
        
        def merge(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            
            while l1 and l2:
                if l1.val > l2.val:
                    curr.next = l2
                    l2 = l2.next
                else:
                    curr.next = l1
                    l1 = l1.next
                    
                curr = curr.next
                
            if l1:
                curr.next = l1
            else:
                curr.next = l2
                
            return dummy.next
        
        
                    
            
            
            
            
        
                
            