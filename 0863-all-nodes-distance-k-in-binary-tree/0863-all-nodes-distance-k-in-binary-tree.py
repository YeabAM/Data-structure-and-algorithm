# Definition for a binary tree node.
# class TreeNode:
#     def init(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        answer = []
        ancestors = []
        ancestors.append((target, 0))
        def bfs(node, tar):
            if tar == 0:
                answer.append(node)
                return
            queue = deque()
            queue.append(node)
            level = 0
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    if curr.val == target.val and node.val != target.val:
                        continue
                    if curr.left and curr.left.val not in visited:
                        queue.append(curr.left)
                    if curr.right and curr.right.val not in visited:
                        queue.append(curr.right)
                level += 1
                if level == tar:
                    answer.extend(queue)
                    return
                
        def dfs(node):
            if not node:
                return -1
            if node.val == target.val:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left != -1 or right != -1:
                depth = max(left,right) + 1
                ancestors.append((node, depth))
                return depth
            return -1
        
        dfs(root)
        visited = set()
        for i in range(len(ancestors)):
            visited.add(ancestors[i][0].val)
            bfs(ancestors[i][0], k - ancestors[i][1])
        answer = list(set(answer))
        ress = []
        for node in answer:
            if node.val != target.val:
                ress.append(node.val)
        return ress