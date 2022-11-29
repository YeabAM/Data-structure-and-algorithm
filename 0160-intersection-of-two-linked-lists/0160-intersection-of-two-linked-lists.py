# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        
        lA = headA
        lB = headB
        nodes = set()
        
        while lA:
            nodes.add(lA)
            lA = lA.next
            
        while lB:
            if lB in nodes:
                return lB
            lB = lB.next
            
        
        return
                
        