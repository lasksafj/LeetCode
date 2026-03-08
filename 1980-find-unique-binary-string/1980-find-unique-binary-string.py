class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ['']*len(nums)
        for i in range(len(nums)):
            res[i] = '0' if nums[i][i] == '1' else '1'
        return ''.join(res)