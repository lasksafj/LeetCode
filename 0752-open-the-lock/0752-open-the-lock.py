class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def neighbor(cur):
            for i in range(4):
                v = int(cur[i])
                for j in (v-1,v+1):
                    if j == -1:
                        s = '9'
                    elif j == 10:
                        s = '0'
                    else:
                        s = str(j)
                    yield cur[:i] + s + cur[i+1:]
        vis = set(deadends)
        if '0000' in vis:
            return -1
        q = deque(['0000'])
        vis.add('0000')
        res = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return res
                for ne in neighbor(cur):
                    if ne not in vis:
                        vis.add(ne)
                        q.append(ne)
            res += 1
        return -1