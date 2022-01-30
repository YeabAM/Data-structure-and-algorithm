# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        #commented code should have worked
        # temp = node
        # temp2 = node.next.next
        # node = node.next
        # temp.next = temp2
        # node.next = temp
        # # #check if nodes are swapped properly
        # print(node.val,temp.val,temp.next.val)
        # print(node.val,node.next.val)
        # node.next = temp.next
        # temp = None
        node.val = node.next.val
        node.next = node.next.next
        
    
        
        
        
        
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        