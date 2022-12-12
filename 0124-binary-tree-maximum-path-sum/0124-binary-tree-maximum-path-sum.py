# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = [-1001]
        
        def dfs(node):
            if not node:
                return 0
            
            if not node.right and not node.left:
                maxSum[0] = max(maxSum[0], node.val)
                return node.val
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            
            
            allSum = left + right + node.val
            leftSum = allSum - right
            rightSum = allSum - left
            
            currMax = max(allSum, leftSum, rightSum, node.val)
            # print(currMax, leftSum)
            
            maxSum[0] = max(maxSum[0], currMax)
            
            return max(leftSum, rightSum, node.val)
        
        dfs(root)
        
        return maxSum[0]
            
            