# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        newNode = None
        
        def dfs(node):
            nonlocal newNode

            if not node:
                return False
            if node.val == p.val or node.val == q.val:
                newNode = node
                return True
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                newNode = node
                return True
            if left or right:
                return True
            
                  
        dfs(root)
        return newNode
        
        
        