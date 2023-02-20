class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def group(word):
            groups = []
            temp = []

            for i in word:
                if not temp or temp[-1] == i:
                    temp.append(i)
                elif temp:
                    groups.append(''.join(temp))
                    temp = [i]

            if temp:
                groups.append(''.join(temp))

            return groups
    
    
        s = group(s) 
        countSubtrings = 0

        for word in words:
            temp = group(word)
            if len(s) != len(temp):
                continue

            isStrechy = True
            for i in range(len(s)):
                if len(temp[i]) == len(s[i]) and temp[i][0] == s[i][0]:
                    continue

                if len(s[i]) < 3 or len(s[i]) < len(temp[i]) or temp[i][0] != s[i][0]:
                    isStrechy = False

            if isStrechy:
                countSubtrings += 1

        return countSubtrings

            
        