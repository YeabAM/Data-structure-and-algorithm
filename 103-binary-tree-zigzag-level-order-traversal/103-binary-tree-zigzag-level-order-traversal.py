# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        resArr = []
        level = []
        poplen = 1
        temp = 0
        queue = collections.deque([root])
        
        while queue:
            level = []
            temp = 0
        
            for i in range(poplen):
                current = queue.popleft()
                # print("cur", current.val)
                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                    temp += 1
                if current.right:
                    queue.append(current.right)
                    temp += 1
            # print("lev", level)    
            poplen = temp
            if len(resArr) % 2 == 0:
                resArr.append(level)
            else:
                resArr.append(level[::-1])
            
        return resArr
                    
                
        