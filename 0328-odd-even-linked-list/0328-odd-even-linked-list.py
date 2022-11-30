# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        oddPointer = head
        evenPointer = head.next
        prevEven = evenPointer
        prevOdd = None
        while evenPointer and oddPointer:
            oddPointer.next = oddPointer.next.next
            if evenPointer.next:
                evenPointer.next = evenPointer.next.next
            prevOdd = oddPointer
            oddPointer = oddPointer.next
            evenPointer = evenPointer.next
            
        
        if oddPointer:
            oddPointer.next = prevEven
        else:
            prevOdd.next = prevEven
        
        return head
        