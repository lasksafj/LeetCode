class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = deque()
        K = set()
        B = set()
        for b in initialBoxes:
            if status[b]:
                q.append(b)
            else:
                B.add(b)
        res = 0
        while q:
            b = q.popleft()
            res += candies[b]
            for nb in containedBoxes[b]:
                if status[nb] or nb in K:
                    q.append(nb)
                else:
                    B.add(nb)
            for nk in keys[b]:
                if nk in B:
                    q.append(nk)
                    B.remove(nk)
                else:
                    K.add(nk)
        return res