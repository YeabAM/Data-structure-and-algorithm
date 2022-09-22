# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        
        while cur:
            nodes.append(cur.val)
            cur = cur.next
        
        temp = nodes[k-1]
        nodes[k-1] = nodes[-k]
        nodes[-k] = temp
        
        newHead = ListNode(0)
        curr = newHead
        
        for val in nodes:
            newNode = ListNode(val)
            curr.next = newNode
            curr = newNode
            
        return newHead.next
        
        
            