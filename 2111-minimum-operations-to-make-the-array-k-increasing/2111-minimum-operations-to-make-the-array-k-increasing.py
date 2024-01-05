def f(nums):
    A = [nums[0]]
    for n in nums[1:]:
        if n >= A[-1]:
            A.append(n)
        else:
            p = bisect_right(A, n)
            A[p] = n
    return len(nums) - len(A)

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        res = 0
        for i in range(k):
            A = []
            for j in range(i,len(arr),k):
                A.append(arr[j])
            res += f(A)
        return res