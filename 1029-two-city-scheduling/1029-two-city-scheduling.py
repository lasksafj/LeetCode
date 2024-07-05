class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        A = sorted(costs, key=lambda x:-abs(x[0]-x[1]))
        N = len(A)
        res = 0
        choose_a = choose_b = 0
        for a,b in A:
            if choose_a == N//2:
                res += b
            elif choose_b == N//2:
                res += a
            elif a < b:
                res += a
                choose_a += 1
            else:
                res += b
                choose_b += 1
        return res