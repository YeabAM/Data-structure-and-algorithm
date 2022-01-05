
class Solution:
    def sqr(self, num):
        return num ** 2
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return list(map(self.sqr , sorted(nums , key = lambda x: x**2)))
                  