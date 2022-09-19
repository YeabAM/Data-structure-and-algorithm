# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        psedo = ListNode(0, head)
        pred = psedo

        while head:
            # print(head.val,pred.val,pred.next.val,psedo.next.val)
            
            if head.next and head.val == head.next.val:
                
                while head.next and head.val == head.next.val:
                    head = head.next
                    
                pred.next = head.next
                
            else:
                pred = pred.next
                    
            head = head.next  
        return psedo.next
        