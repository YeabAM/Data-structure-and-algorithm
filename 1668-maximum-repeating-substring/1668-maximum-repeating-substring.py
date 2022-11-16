class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        N, M = len(sequence), len(word)
        left = 0
        count = 0
        ans = 0
        
        for j in range(N):
            count = 0
            left = 0
            start = j
            while (start < N and sequence[start] == word[left]):
                    left += 1
                    start += 1
                    if left == M:
                        count += 1
                        left = 0
                    
            ans = max(ans, count)
        return ans
        