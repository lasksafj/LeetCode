class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set()
        for n in nums:
            a = n[::-1]
            s.add(sum((1<<i)*(a[i] == '1') for i in range(len(a))))
        for i in range(1<<len(nums)):
            if i not in s:
                res = bin(i)[2:]
                if len(res) < len(nums):
                    return '0'*(len(nums)-len(res)) + res
                return res
        return ''