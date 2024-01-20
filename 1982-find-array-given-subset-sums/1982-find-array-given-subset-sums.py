class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        def sol(sums):
            if len(sums) == 1:
                return []
            sums.sort()
            cnt = Counter(sums)
            x = sums[-1] - sums[-2]
            excluding = []
            including = []
            for s in sums:
                if cnt[s] == 0:
                    continue
                cnt[s] -= 1
                cnt[s+x] -= 1
                excluding.append(s)
                including.append(s+x)
            if 0 not in including:
                return [x] + sol(excluding)
            else:
                return [-x] + sol(including)
        return sol(sums)