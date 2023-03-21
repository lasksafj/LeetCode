class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        # p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        f = [-1, 0, 1, 2, -1, 4, 3, 8, -1, -1, 5, 16, -1, 32, 9, 6, -1, 64, -1, 128, -1, 10, 17, 256, -1, -1, 33, -1, -1, 512, 7]
        m = defaultdict(int)
        masks = {}
        for n in nums:
            # print(f[n])
            if f[n] != -1:
                for i in m.copy():
                    if i&f[n] == 0:
                        m[i|f[n]] += m[i]
                m[f[n]] += 1
                # print(n,m[f[n]])
        # print(m)
        return sum(m[i] for i in m) % 1000000007