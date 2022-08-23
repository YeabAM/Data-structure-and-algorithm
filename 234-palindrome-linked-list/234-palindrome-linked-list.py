# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        half = []
        sp = head
        fp = head
        prev = None
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
        while sp:
            temp = sp.next
            sp.next=prev
            prev=sp
            sp=temp
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
            
            
            
            
            