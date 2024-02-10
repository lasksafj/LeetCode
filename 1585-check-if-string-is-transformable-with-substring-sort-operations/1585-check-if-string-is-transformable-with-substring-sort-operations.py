from sortedcontainers import SortedList
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        N = len(s)
        pos = [deque() for _ in range(10)]
        for i,ch in enumerate(s):
            pos[int(ch)].append(i)
        for ch in t:
            n = int(ch)
            if not pos[n]:
                return False
            for k in range(n):
                if pos[k] and pos[k][0] < pos[n][0]:
                    return False
            pos[n].popleft()
        return True