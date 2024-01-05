def f(nums):
    # print(nums)
    A = [nums[0]]
    for n in nums[1:]:
        if n >= A[-1]:
            A.append(n)
        else:
            p = bisect_left(A, n)
            if A[p] > n:
                A[p] = n
            else:
                A[p+1] = n
    # print(A)
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