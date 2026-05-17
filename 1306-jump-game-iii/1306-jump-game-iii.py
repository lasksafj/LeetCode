class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)
        q = deque([start])
        vis = {start}
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            for j in [i-arr[i],i+arr[i]]:
                if 0<=j<N and j not in vis:
                    q.append(j)
                    vis.add(j)
        return False