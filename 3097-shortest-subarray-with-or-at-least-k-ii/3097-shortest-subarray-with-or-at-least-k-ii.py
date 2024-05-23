def add_num(A,n):
    k = 0
    while n > 0:
        A[k] += n&1
        n >>= 1
        k += 1
def remove_num(A,n):
    k = 0
    while n > 0:
        A[k] -= n&1
        n >>= 1
        k += 1
def calc(A):
    res = 0
    for i in range(len(A)-1,-1,-1):
        res <<= 1
        res |= (A[i] > 0)
    return res

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        j = 0
        A = [0]*32
        res = inf
        for i in range(len(nums)):
            add_num(A,nums[i])
            # print(A)
            while j <= i and calc(A) >= k:
                res = min(res, i-j+1)
                remove_num(A,nums[j])
                j += 1
            
        return res if res < inf else -1