class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        L = [[] for _ in range(n+1)]
        for a,b in conflictingPairs:
            L[max(a,b)].append(min(a,b))
        cur,prev = 0,0
        res = 0
        gain = [0]*(n+1)
        for i in range(1, n+1):
            for j in L[i]:
                if cur < j:
                    prev = cur
                    cur = j
                elif prev < j:
                    prev = j
            res += i-cur
            gain[cur] += cur-prev
        return res + max(gain)