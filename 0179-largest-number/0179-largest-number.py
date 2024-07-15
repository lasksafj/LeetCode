class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        A = sorted([str(n) for n in nums], key=LargerNumKey)
        return str(int(''.join(A)))