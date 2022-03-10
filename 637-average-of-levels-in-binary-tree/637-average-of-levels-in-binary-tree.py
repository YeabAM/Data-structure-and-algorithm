# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        visited = set()
        q = deque()
        level = []
        lv = []
        def bfs(root):
            if not root:
                return
            q.append(root)
            # level.append(lv)
            while q:
                size = len(q)
                tot = 0
                for _ in range(size):
                    cur = q.popleft()
                    if cur.left:
                        q.append(cur.left)                       
                            # bfs(cur.left)
                    if cur.right:
                        q.append(cur.right)
                    tot += cur.val
                level.append(tot / size)
                    
                # lv.append(cur.val)
                # if cur not in visited:
                #     visited.add(cur.val)
                   
            # print(visited)
          
        bfs(root)
        return level
                    
                
        
        