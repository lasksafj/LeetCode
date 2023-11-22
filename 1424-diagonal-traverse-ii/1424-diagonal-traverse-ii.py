class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        q = deque([[0,0]])
        while q:
            vis = set()
            for _ in range(len(q)):
                a,b = q.popleft()
                res.append(nums[a][b])
                if a+1 < len(nums) and b < len(nums[a+1]) and (a+1,b) not in vis:
                    q.append([a+1,b])
                if b+1 < len(nums[a]):
                    q.append([a,b+1])
                    vis.add((a,b+1))
        return res