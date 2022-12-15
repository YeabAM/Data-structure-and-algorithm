# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def flaten(node):
            if not node:
                return (None,None)
            
            if node and not node.left and not node.right:
                return (node, node)
            
            left = flaten(node.left) 
            right = flaten(node.right)
            
            if left[0]:
                left[1].right = right[0]
                node.right = left[0]
            
            node.left = None
            temp = right[1] or left[1]
            return node, temp
        
        flaten(root)