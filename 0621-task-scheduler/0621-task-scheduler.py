class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        A = [0]*26
        for t in tasks:
            A[ord(t)-ord('A')] += 1
        A.sort()
        ma = A[-1]-1
        empty = ma*n
        for i in range(24,-1,-1):
            empty -= min(ma, A[i])
        return len(tasks) + max(empty, 0)