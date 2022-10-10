# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = 0
        
        def dfs(start, end):
            nonlocal idx
            
            if idx >= len(preorder):
                return None
            
            root = TreeNode()
            root.val = preorder[idx]
            # print(root)
            pos = -1
            for i in range(start, end):
                if inorder[i] == preorder[idx]:
                    pos = i
                    break
                    
            # print(preorder[idx], pos,  start, end)       
            
            if pos == -1:
                return None
            
            idx += 1  
            root.left = dfs(start, pos)
            
            root.right = dfs(pos + 1, end)
        
                                 
            return root
        
        return dfs(0, len(preorder))
            
            