# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        node = root
        
        while node:
            
            if node.val < val:
                node = node.right
            elif node.val > val:
                node = node.left
            else:
                return node
            
        