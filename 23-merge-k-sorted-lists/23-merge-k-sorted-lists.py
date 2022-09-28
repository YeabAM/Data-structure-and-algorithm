# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        Kelements = []
        for idx, node in enumerate(lists):
            if node:
                heappush(Kelements,(node.val, idx, node))
        while Kelements:
            currSmall = heappop(Kelements)
            currList = currSmall[1]
            currNode = currSmall[2]
            newNode = ListNode(currSmall[0])
            curr.next = newNode
            curr = newNode
            if currNode.next:
                heappush(Kelements, (currNode.next.val,currList,currNode.next))
                
        return dummy.next