class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        width = 0
        curr_line = []
        i = 0
        
        while i < len(words):
            curr_word = words[i]
            
            if width + len(curr_word) <= maxWidth:
                curr_line.append(curr_word)
                width += len(curr_word) + 1
                i += 1
                
            else:
                space_needed = maxWidth - width + len(curr_line)
                # print(space_needed, width,len(curr_line),'w')
                space_added = 0
                j = 0
                
                while space_added < space_needed:
                    if j >= len(curr_line) - 1:
                        j = 0
                    
                    curr_line[j] += ' '
                    space_added += 1
                    j += 1
                    
                justified_line = "".join(curr_line)   
                res.append(justified_line)
                
                curr_line = []
                width = 0
                
        for k in range(len(curr_line) - 1):
            curr_line[k] += ' '
        
        # print((maxWidth - width + 1))
        curr_line[-1] += ' ' * (maxWidth - width + 1)

        justified_line = "".join(curr_line)
        # print(len(justified_line))
        res.append(justified_line)
        
        
        return res
        
        
