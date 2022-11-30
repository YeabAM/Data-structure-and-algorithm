# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        
        while curr:
            nodes.append(curr.val)
            curr = curr.next
            
        #kth elements
        nodes[k-1], nodes[-k] = nodes[-k], nodes[k-1]
        
        newHead = ListNode(0)
        curr = newHead
        
        for node in nodes:
            newNode = ListNode(node)
            curr.next = newNode
            curr = newNode
            
        return newHead.next
        