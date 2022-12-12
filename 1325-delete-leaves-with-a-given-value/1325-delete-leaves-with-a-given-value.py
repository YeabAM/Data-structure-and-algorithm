# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        dummy = TreeNode(0, node)
        
        def delete(root, target):
            if not root:
                return True

            left = delete(root.left, target)
            right = delete(root.right, target)

            if left:
                root.left = None
                
            if right:
                root.right = None
            
            return root.val == target and left and right
        
        delete(dummy, target)
        
        
        return dummy.left
        
        