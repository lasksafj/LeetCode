class Solution:
    def countPalindromes(self, s: str) -> int:
        n = len(s)
        nums = [a+b for a in '0123456789' for b in '0123456789']
        left = [defaultdict(int) for _ in range(n)]
        right = [defaultdict(int) for _ in range(n)]
        sd = defaultdict(int)
        sd[s[0]] = 1
        for i in range(1,n):
            c = s[i]
            for num in nums:
                left[i][num] = left[i-1][num] + (sd[num[0]] if num[1]==c else 0)
            sd[c] += 1
        sd.clear()
        sd[s[-1]] = 1
        for i in range(n-2, -1, -1):
            c = s[i]
            for num in nums:
                right[i][num] = right[i+1][num] + (sd[num[0]] if num[1]==c else 0)
            sd[c] += 1
        res = 0
        # print(left[2],right[2])
        for i in range(2, n-2):
            for num in nums:
                res = (res + left[i-1][num] * right[i+1][num]) % 1000000007
        return res % 1000000007