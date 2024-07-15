class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        n = N//3
        
        pq = nums[n*2:]
        heapify(pq)
        s = sum(nums[n*2:])
        R = [s]
        for i in range(n*2-1, n-1, -1):
            heappush(pq, nums[i])
            s += nums[i]
            s -= heappop(pq)
            R.append(s)
        
        pq = []
        for k in nums[:n]:
            heappush(pq, -k)
        
        s = sum(nums[:n])
        k = n
        res = s-R[k]
        for i in range(n, n*2):
            heappush(pq, -nums[i])
            s += nums[i]
            s -= -heappop(pq)
            k -= 1
            res = min(res, s-R[k])
        return res