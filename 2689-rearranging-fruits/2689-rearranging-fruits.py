class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1 = Counter(basket1)
        cnt2 = Counter(basket2)
        for k in set(list(cnt1.keys()) + list(cnt2.keys())):
            cnt1[k] -= cnt2[k]
            if cnt1[k] == 0:
                del cnt1[k]
        A = []
        for k,v in cnt1.items():
            if abs(v)&1:
                return -1
            A += [k]*(abs(v)//2)
        A.sort()
        mi = min(basket1 + basket2)
        # s = sum(A[:len(A)//2])
        # res = s
        # t = 0
        # for i in range(len(A)//2-1, -1,-1):
        #     t += mi*2
        #     s -= A[i]
        #     res = min(res, s+t)
        # return res
        return sum(min(mi*2, A[i]) for i in range(len(A)//2))