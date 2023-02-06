class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        counts = defaultdict(int)
        max_chain = 1
        
        for word in words:
            curr_chain = 1
            
            for i in range(len(word)):
                curr = word[:i] + word[i+1:]
                curr_chain = max(curr_chain, counts[curr] + 1)
                
            max_chain = max(max_chain, curr_chain)
            counts[word] = curr_chain
            
        return max_chain