class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        res = -inf
        for a,b in itertools.permutations(list(set(s)), 2):
            # print(a,b)
            fa = s[:k].count(a)
            fb = s[:k].count(b)
            prev_a = 0
            prev_b = 0
            mp = defaultdict(lambda: inf)
            mp[0] = 0
            if fa&1 and fb&1==0 and fb > 0:
                res = max(res, fa-fb)
            # print(res)
            j = 0
            for i in range(k, len(s)):
                fa += s[i] == a
                fb += s[i] == b
                while j <= i-k and prev_b + (s[j]==b) < fb:
                    prev_a += s[j] == a
                    prev_b += s[j] == b
                    prev_mask = ((prev_a&1) << 1) | (prev_b&1)
                    mp[prev_mask] = min(mp[prev_mask], prev_a - prev_b)
                    j += 1
                mask = ((fa&1) << 1) | (fb&1)
                # print('----',i, mask)
                # 2: 0b10
                if fb > 0:
                    res = max(res, fa - fb - mp[mask^2])
                # print('---------------', res)
        return res