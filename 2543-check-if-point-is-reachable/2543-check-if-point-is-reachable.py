class Solution:
    def isReachable(self, x: int, y: int) -> bool:
#         gcd(x,y) = 2 ^ k
        return gcd(x,y).bit_count() == 1