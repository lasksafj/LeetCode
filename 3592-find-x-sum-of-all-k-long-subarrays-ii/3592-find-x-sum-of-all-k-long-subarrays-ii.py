class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        N = len(nums)
        s = 0
        mp = defaultdict(int)
        L = SortedList()
        R = SortedList()
        def R_add(p):
            nonlocal s
            f,a = p
            R.add((f,a))
            s += f*a
        def R_remove(p):
            nonlocal s
            f,a = p
            R.remove((f,a))
            s -= f*a
            return (f,a)
        def add(a):
            nonlocal s
            f = mp[a]
            mp[a] += 1
            if (f,a) in R:
                R_remove((f,a))
                R_add((f+1,a))
                return
            if (f,a) in L:
                L.remove((f,a))
            L.add((f+1,a))
            R_add(L.pop())
            if len(R) > x:
                L.add(R_remove(R[0]))
        def remove(a):
            nonlocal s
            f = mp[a]
            mp[a] -= 1
            if (f,a) in L:
                L.remove((f,a))
                L.add((f-1,a))
                return
            R_remove((f,a))
            L.add((f-1,a))
            R_add(L.pop())
            if len(R) > x:
                L.add(R_remove(R[0]))
        res = []
        for i in range(N):
            if i >= k:
                remove(nums[i-k])
            add(nums[i])
            if i >= k-1:
                res.append(s)
        return res