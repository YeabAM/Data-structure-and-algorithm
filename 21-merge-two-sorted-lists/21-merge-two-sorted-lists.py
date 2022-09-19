# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = dummy
        
        while list1 != None or list2 != None:
            v1 = list1.val if list1 else 200
            v2 = list2.val if list2 else 200
            
            if v1 > v2:
                newNode = ListNode(v2)
                curr.next = newNode
                curr = newNode
                list2 = list2.next if list2 else None
                
            elif v1 < v2:
                newNode = ListNode(v1)
                curr.next = newNode
                curr = newNode
                list1 = list1.next if list1 else None
                
            elif v1 == v2 and v1 != 200 and v2 != 200:
                newNode = ListNode(v1)
                curr.next = newNode
                curr = newNode
                list1 = list1.next if list1 else None
                # list2 = list2.next if list2 else None
                
                
                
        return dummy.next
                