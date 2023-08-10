class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        s = sum(n for n in nums if n > 0)
        A = sorted(abs(n) for n in nums)
        # print(A,s)
        pq = [(-(s - A[0]),0)]
        for _ in range(k-1):
            s,i = heappop(pq)
            s = -s
            if i+1 < len(A):
                heappush(pq, (-(s - A[i+1]), i+1 ))
                heappush(pq, (-(s - A[i+1] + A[i]), i+1 ))
            # print(pq)
        return s