class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        N = len(nums)
        mp = Counter([n%value for n in nums])
        for i in range(N):
            if mp[i%value]:
                mp[i%value] -= 1
            else:
                return i
        return N