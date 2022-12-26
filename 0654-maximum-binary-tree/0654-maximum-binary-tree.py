# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(root, nums):
            max_val = max(nums)
            idx = -1
            
            
            for i in range(len(nums)):
                if max_val == nums[i]:
                    idx = i
                    break
                    
            root.val = max_val
            
            left = nums[:idx]
            right = nums[idx+1:]
            
            if left:
                root.left = TreeNode()
                build(root.left, left)
                 
                
            if right:
                root.right = TreeNode()
                build(root.right, right)
                
            
        root = TreeNode()
        
        build(root, nums)
        
        return root
                
                
        
            
            
                
            
                
        
                
        