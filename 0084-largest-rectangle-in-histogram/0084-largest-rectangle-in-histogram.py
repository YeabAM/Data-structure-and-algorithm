class Solution:
    def build_left(self, ranges, heights):
        stack = []
        
        
        for i in range(len(heights)):
            curr_max = None
            
            while stack and stack[-1][0] > heights[i]:
                temp, idx = stack.pop()
                
                if not curr_max:
                    curr_max = (temp, idx)
                    
                ranges[idx] += abs(curr_max[1] - idx)
                
            stack.append((heights[i], i))
            
        curr_max = None
        
        while stack:
            temp, idx = stack.pop()
            
            if not curr_max:
                curr_max = (temp, idx)

            ranges[idx] += abs(curr_max[1] - idx)
            
    def build_right(self, ranges, heights):
        stack = []
        
        
        for i in range(len(heights) -1 , -1, -1):
            curr_max = None
            while stack and stack[-1][0] > heights[i]:
                temp, idx = stack.pop()
                
                if not curr_max:
                    curr_max = (temp, idx)
                    
                ranges[idx] += abs(curr_max[1] - idx)
                
            stack.append((heights[i], i))
            
        curr_max = None
        
        while stack:
            temp, idx = stack.pop()
            
            if not curr_max:
                curr_max = (temp, idx)

            ranges[idx] += abs(curr_max[1] - idx)      
        
    def largestRectangleArea(self, heights: List[int]) -> int:
        ranges = defaultdict(int)
        self.build_left(ranges, heights)
        self.build_right(ranges, heights)
        max_area = float('-inf')
        
        for idx in ranges:
            max_area = max(max_area, heights[idx] * (ranges[idx] + 1))
                           
        return max_area
            
        
    
        