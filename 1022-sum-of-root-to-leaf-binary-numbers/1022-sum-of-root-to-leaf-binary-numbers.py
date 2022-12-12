# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
    
        total = 0
        
        def dfs(node, path):
            nonlocal total
            if not node:
                return 
            
            if not node.left and not node.right: 
                path += str(node.val)
                # print(path)
                total += int(path, 2)
                return
            
            dfs(node.left, path + str(node.val))
            
            dfs(node.right, path + str(node.val))
                
            return 
        
        dfs(root,'')
        return total

                
        
        
        
        