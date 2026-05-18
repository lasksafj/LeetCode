class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        mp = defaultdict(list)
        for i,a in enumerate(arr):
            mp[a].append(i)
        q = deque([0])
        res = 0
        vis = {0}
        num_vis = set()
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if i == N-1: return res
                for j in [i-1,i+1]:
                    if 0<=j<N and j not in vis:
                        q.append(j)
                        vis.add(j)
                if arr[i] not in num_vis:
                    num_vis.add(arr[i])
                    for j in mp[arr[i]]:
                        if 0<=j<N and j not in vis:
                            q.append(j)
                            vis.add(j)
            res += 1
        return res