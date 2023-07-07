class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
# p = i*n+j
# in_mask, ex_mask: n positions before p
        base_mask = (1<<n)-1
        def est_point(p, in_mask, ex_mask, a):
            # 0: no person, 1: introvert, 2: extrovert 
            up_person = ((in_mask&(1<<(n-1))) >> (n-1)) + 2 * ((ex_mask&(1<<(n-1))) >> (n-1))
            left_person = 0
            left_person = ((in_mask&1) + 2*(ex_mask&1)) if p%n > 0 else 0
            res = 0
            if a == 1 or a == 2:
                if up_person == 2:
                    res += 20 + (20 if a == 2 else -30)
                elif up_person == 1:
                    res += -30 + (20 if a == 2 else -30)
                if left_person == 2:
                    res += 20 + (20 if a == 2 else -30)
                elif left_person == 1:
                    res += -30 + (20 if a == 2 else -30)
            return res
        # print(est_point(1,0,1,1))
        # return 0
        @cache
        def dfs(p, in_cnt, ex_cnt, in_mask, ex_mask):
            in_mask &= base_mask
            ex_mask &= base_mask
            if p == m*n:
                return 0
            res = 0
            res = max(res, dfs(p+1, in_cnt, ex_cnt, in_mask<<1, ex_mask<<1))
            if in_cnt > 0:
                e = est_point(p, in_mask, ex_mask, 1) + 120
                res = max(res, e + dfs(p+1, in_cnt-1, ex_cnt, (in_mask<<1)|1, ex_mask<<1))
            if ex_cnt > 0:
                e = est_point(p, in_mask, ex_mask, 2) + 40
                res = max(res, e + dfs(p+1, in_cnt, ex_cnt-1, in_mask<<1, (ex_mask<<1)|1))
            # print(p, in_cnt, ex_cnt, in_mask, ex_mask, '--', res)
            return res
        return dfs(0,introvertsCount,extrovertsCount,0,0)