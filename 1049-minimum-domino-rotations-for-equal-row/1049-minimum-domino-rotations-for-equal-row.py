class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        N = len(tops)
        def sol(a):
            t,b = 0,0
            print(a)
            for i in range(N):
                if tops[i] != a and bottoms[i] != a:
                    return inf
                elif tops[i] == a and bottoms[i] == a:
                    continue
                elif tops[i] == a:
                    b += 1
                else:
                    t += 1
            return min(b,t)
        res = min(sol(tops[0]), sol(bottoms[0]))
        return res if res < inf else -1