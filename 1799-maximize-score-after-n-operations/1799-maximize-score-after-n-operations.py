class Solution:
    def maxScore(self, nums: List[int]) -> int:
        res = [0,0]
        path = []
        n = len(nums)
        
        def sol():
            res[1] += 1
            # print(nums)
            if len(path) == n//2:
                tmp = path[:]
                tmp.sort()
                # print(tmp)
                s = sum([(i+1)*e for i,e in enumerate(tmp)])
                res[0] = max(res[0], s)
                return
            for i in range(n):
                if nums[i] == 0:
                    continue
                for j in range(i+1,n):
                    if nums[j] == 0:
                        continue
                    a,b = nums[i],nums[j]
                    nums[i],nums[j] = 0,0
                    path.append(gcd(a,b))
                    sol()
                    nums[i],nums[j] = a,b
                    path.pop()
                break
        sol()
        # print(res[1])
        return res[0]