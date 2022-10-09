class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        wordrelation = list(zip(*strs))
        prefix = []
        
        for word in wordrelation:
            if len(set(word)) == 1:
                prefix.append(word[0])
            else:
                break
                
        return "".join(prefix)