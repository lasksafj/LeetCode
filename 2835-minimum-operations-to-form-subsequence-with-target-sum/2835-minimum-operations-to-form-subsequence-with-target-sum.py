class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        T = list(bin(target))[2:][::-1]
        A = [0] * 32
        for n in nums:
            N = list(bin(n))[2:][::-1]
            for i,ch in enumerate(N):
                if ch == '1':
                    A[i] += 1
        # print(A)
        # print(T)
        ne = -1
        res = 0
        for i,ch in enumerate(T):
            if ch == '0':
                continue
                
            # print(i,ch)
            
            if A[i] > 0:
                A[i] -= 1
                continue
            j = i
            cur = 1
            while j >= 0 and cur > 0:
                cur = max(0, cur - A[j])
                cur *= 2
                j -= 1
            # print(cur)
            if cur == 0:
                j = i
                cur = 1
                while j >= 0 and cur > 0:
                    if A[j] > cur:
                        A[j] -= cur
                        cur = 0
                    else:
                        cur -= A[j]
                        A[j] = 0
                    cur *= 2
                    j -= 1
            else:
                j = i
                while j < 32 and A[j] == 0:
                    A[j] = 1
                    j += 1
                if j == 32:
                    return -1
                res += j-i
                A[j] -= 1
            # print('----',i,res)
        return res