class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        m = defaultdict(int)
        for n in nums:
            a = n%value
            m[a] += 1
        for i in range(0, 100000):
            a = i%value
            m[a] -= 1
            if m[a] < 0:
                return i
        return 100000