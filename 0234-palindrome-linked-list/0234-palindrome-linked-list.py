# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next
        
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print  
        
        
        curr = slow.next
        slow.next = None
        prev = None
        
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
            
        temp = head
        
        while temp and prev:
            if temp.val != prev.val:
                return False
            
            prev = prev.next
            temp = temp.next
            
        return True
        
        
            
            
            
        
            
        
        