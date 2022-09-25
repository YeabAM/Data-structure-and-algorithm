# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return 
        
        def backtrack(curr, path):
            currSum = sum(path)
            # print(path,currSum)
            if currSum == targetSum:
                if not curr.left and not curr.right:
                    res.append(path)
            # if currSum < targetSum:
            
            if curr.left:
                backtrack(curr.left, path + [curr.left.val])
            if curr.right:
                # print("h")
                
                backtrack(curr.right,path + [curr.right.val]) 
        
        
        backtrack(root,[root.val])
        return res
            
            
            
            
        
        
        