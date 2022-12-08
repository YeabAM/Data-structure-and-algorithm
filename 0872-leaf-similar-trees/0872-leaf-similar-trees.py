# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []
        
        def collectLeaf(root, leaf):
            
            if not root.left and not root.right:
                leaf.append(root.val)
                return
                
            if root.left:
                collectLeaf(root.left, leaf)
                
            if root.right:
                collectLeaf(root.right, leaf)
            
                
        collectLeaf(root1, leaf1)
        collectLeaf(root2, leaf2)
        
        if len(leaf1) != len(leaf2):
            return False
        
        for i in range(len(leaf1)):
            if leaf1[i] != leaf2[i]:
                return False
            
        return True
            
            
                
            
                
                
        