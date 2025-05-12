class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        res = []
        for a in range(1, 10):
            if a not in cnt:
                continue
            cnt[a] -= 1
            for b in range(10):
                if cnt[b] == 0:
                    continue
                cnt[b] -= 1
                for c in range(0,10,2):
                    if cnt[c] > 0:
                        res.append(a*100+b*10+c)
                cnt[b] += 1
            cnt[a] += 1
        return sorted(res)