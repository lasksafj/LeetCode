class Solution:
    def minJumps(self, arr: List[int]) -> int:
        m = defaultdict(list)
        for i,n in enumerate(arr):
            m[n].append(i)
        # print(m)
        q = deque([0])
        n = len(arr)
        vis = [False]*n
        vis[0] = True
        res = 0
        while q:
            # print(q)
            for _ in range(len(q)):
                c = q.popleft()
                if c == n-1:
                    return res
                if c > 0 and not vis[c-1]:
                    q.append(c-1)
                    vis[c-1] = True
                if c < n-1 and not vis[c+1]:
                    q.append(c+1)
                    vis[c+1] = True
                for ne in m[arr[c]]:
                    if not vis[ne]:
                        q.append(ne)
                        vis[ne] = True
                del m[arr[c]]
            res += 1
        return res
            