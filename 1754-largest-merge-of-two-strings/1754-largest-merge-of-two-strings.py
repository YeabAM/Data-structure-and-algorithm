class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ans = ""
        while word1 and word2:
            # print(word1, word2, ans)
            if word1 < word2:
                ans += word2[0]
                word2 = word2[1:]

            else:
                ans += word1[0]
                word1 = word1[1:]
                
        
        return ans + word1 + word2
        