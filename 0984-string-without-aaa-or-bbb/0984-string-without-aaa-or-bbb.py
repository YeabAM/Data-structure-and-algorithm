class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []
        i = max(a,b)
        j = min(a,b)
            
        x = ceil(i / 2)
        ilist = [1] * x 
        jlist = [1] * min(x, j)
        i -= x
        j -= x
        for val in range(len(ilist)):
            if i > 0:
                ilist[val] += 1
                i -= 1
            if j > 0:
                jlist[val] += 1
                j -= 1
        if a > b:
            for val in range(len(ilist)):
                result.append('a'*ilist[val])
                a -= ilist[val]
                if b > 0:
                    result.append('b'*jlist[val])
                    b -= jlist[val]
        else:
            for val in range(len(ilist)):
                result.append('b'*ilist[val])
                b -= ilist[val]
                if a > 0:
                    result.append('a'*jlist[val])
                    a -= jlist[val]
        return ''.join(result)

