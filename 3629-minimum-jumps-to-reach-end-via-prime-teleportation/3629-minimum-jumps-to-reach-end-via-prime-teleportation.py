N = 10**6+1
prime = [1]*N
prime[0] = prime[1] = 0
for i in range(2, N):
    if prime[i]:
        for j in range(i*i, N, i):
            prime[j] = 0
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        ne = defaultdict(list)
        for i in range(1, len(nums)):
            d = nums[i]
            for k in range(2, int(sqrt(d))+1):
                while d%k == 0:
                    d //= k
                    ne[k].append(i)
            if d >= 2:
                ne[d].append(i)
        q = deque([0])
        vis = [0]*len(nums)
        vis[0] = 1
        vis_prime = set()
        res = [0]*len(nums)
        k = 0
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                res[i] = k
                for j in [i-1,i+1]:
                    if 0<=j<len(nums) and not vis[j]:
                        q.append(j)
                        vis[j] = 1
                if prime[nums[i]] and nums[i] not in vis_prime:
                    vis_prime.add(nums[i])
                    for j in ne[nums[i]]:
                        if not vis[j]:
                            vis[j] = 1
                            q.append(j)
            k += 1
        return res[-1]