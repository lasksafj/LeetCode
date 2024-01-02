class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.sort()
        vFences.sort()
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]
        s = set()
        for i in range(len(vFences)):
            for j in range(i):
                s.add(vFences[i]-vFences[j])
        res = -1
        for i in range(len(hFences)):
            for j in range(i):
                d = hFences[i]-hFences[j]
                if d in s:
                    res = max(res, d)
        return res*res%(10**9+7) if res > -1 else -1