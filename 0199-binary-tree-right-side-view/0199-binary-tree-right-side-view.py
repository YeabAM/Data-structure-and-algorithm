# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        rsv = [root.val]
        
        queue = deque()
        
        queue.append(root)
        
        while queue:
            level = []
            # print('----')
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                # print(curr.val,'pop')
                if curr.left:
                    queue.append(curr.left)
                    level.append(curr.left.val)
                    
                if curr.right:
                    queue.append(curr.right)
                    level.append(curr.right.val)
                    
            # print(level)
            
            if level:
                rsv.append(level[-1])
            
        return rsv
            
        