class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        A = nums[:]
        N = len(A)
        L = [i-1 for i in range(N+1)]
        R = [i+1 for i in range(N+1)]
        inv = 0
        SL = SortedList()
        for i in range(N-1):
            SL.add([A[i] + A[i+1], i])
            inv += A[i] > A[i+1]
        A.append(inf)
        
        def remove(i):
            nonlocal inv
            if i < 0: return
            j = R[i]
            if j == N: return
            SL.discard([A[i] + A[j], i])
            inv -= A[i] > A[j]
        def add(i):
            nonlocal inv
            if i < 0: return
            j = R[i]
            if j == N: return
            SL.add([A[i] + A[j], i])
            inv += A[i] > A[j]
        res = 0
        while inv:
            res += 1
            s,i = SL.pop(0)
            l = L[i]
            r = R[i]
            rr = R[r]
            if A[i] > A[r]:
                inv -= 1
            remove(l)
            remove(r)
            A[i] += A[r]
            R[i] = rr
            L[rr] = i
            add(l)
            add(i)
        return res