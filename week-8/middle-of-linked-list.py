# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # size of the linked list
        temp = head
        temp2 = head
        while temp2 != None and temp2.next != None :
            temp = temp.next
            temp2= temp2.next.next
        
        return temp
    
        