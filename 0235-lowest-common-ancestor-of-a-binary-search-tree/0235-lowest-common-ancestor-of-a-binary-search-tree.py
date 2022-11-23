# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        p, q = min(p.val,q.val), max(p.val,q.val)

        def lca(node):
            if p <= node.val <= q:
                return node
            
            if node.val < p:
                return lca(node.right)
                
            else:
                return lca(node.left)
            
        return lca(root)