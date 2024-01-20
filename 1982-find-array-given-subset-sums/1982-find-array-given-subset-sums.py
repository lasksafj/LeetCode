class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        def sol(sums):
            if len(sums) == 1:
                return []
            sums.sort()
            cnt = Counter(sums)
            # x >= 0, arr may have x or -x
            x = sums[-1] - sums[-2]
            # arr does not have x
            excluding = []
            # arr does have x
            including = []
            # x >= 0 -> s and s+x must be in sums
            for s in sums:
                if cnt[s] == 0:
                    continue
                cnt[s] -= 1
                cnt[s+x] -= 1
                excluding.append(s)
                including.append(s+x)
            # including must not have sum 0, 
            # if including has, then it should be excluding and original arr has -x, not x
            if 0 not in including:
                return [x] + sol(excluding)
            else:
                return [-x] + sol(including)
        return sol(sums)