class Solution:
    def trap(self, heights: List[int]) -> int:
        stack = []
        total = 0
        for i in range(len(heights)):
            if not stack or stack[-1][1] > heights[i]:
                stack.append((i, heights[i]))
                continue
            
            while stack and stack[-1][1] <= heights[i]:
                temp = stack.pop()
                if stack:
                    height = min(stack[-1][1], heights[i])
                    width = i - stack[-1][0] - 1
                    height -= temp[1]
                    area = width * height
                    total += area
                
            stack.append((i, heights[i]))
                
        return total