def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        A = []
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                A.append(1)
            elif nums[i] == nums[i+1]:
                A.append(0)
            else:
                A.append(-1)
        A = z_function(pattern + [2] + A)
        res = 0
        for i in range(len(pattern)+1, len(A)):
            if A[i] == len(pattern):
                res += 1
        return res