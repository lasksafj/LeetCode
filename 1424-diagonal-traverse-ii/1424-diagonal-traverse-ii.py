class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        q = deque([[0,0]])
        while q:
            for _ in range(len(q)):
                a,b = q.popleft()
                res.append(nums[a][b])
                if b == 0 and a+1 < len(nums):
                    q.append([a+1,b])
                if b+1 < len(nums[a]):
                    q.append([a,b+1])
        return res