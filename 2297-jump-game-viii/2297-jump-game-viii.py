class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        N = len(nums)
        adj = defaultdict(list)
        st = []
        for i in range(N):
            while st and nums[st[-1]] <= nums[i]:
                j = st.pop()
                adj[j].append(i)
            st.append(i)
        st = []
        for i in range(N):
            while st and nums[st[-1]] > nums[i]:
                j = st.pop()
                adj[j].append(i)
            st.append(i)
        pq = [[0,0]]
        dist = [inf]*N
        dist[0] = 0
        while pq:
            d,i = heappop(pq)
            for j in adj[i]:
                if dist[j] > d+costs[j]:
                    heappush(pq, [d+costs[j], j])
                    dist[j] = d+costs[j]
        return dist[-1]