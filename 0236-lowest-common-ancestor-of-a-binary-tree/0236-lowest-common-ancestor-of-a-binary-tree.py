# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        path1, path2 = [], []
        
        def dfs(node,target):
            # print(target, path, "dfs")
            if not node:
                return []
            if node.val == target:
                return [node.val]
            
            path = [node.val]
            leftPath = dfs(node.left, target)
            rightPath = dfs(node.right, target)
            if leftPath:
                return path + leftPath
            if rightPath:
                return path + rightPath
            
            
            # return path
                
        
                
               
        path1 = dfs(root,p.val)
        path2 = dfs(root,q.val)
    
        path1 = set(path1)
        
        for n in path2[::-1]:
            if n in path1:
                return TreeNode(n)
            
        
        
        