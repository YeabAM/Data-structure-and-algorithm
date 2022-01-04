class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        bigNum = list((map(str,nums)))
        for i in range(len(bigNum),0,-1):
            for i in range(i-1):
                if bigNum[i] + bigNum[i+1] < bigNum[i+1] + bigNum[i]:
                    bigNum[i],bigNum[i+1] = bigNum[i+1], bigNum[i]
        bigNum = "".join(bigNum)
        if bigNum[0] == "0":
            bigNum = "0"
        return bigNu