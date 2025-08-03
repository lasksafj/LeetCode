class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        N = len(fruits)
        res = score = 0
        j = 0
        for i in range(N):
            score += fruits[i][1]
            while j <= i:
                a = startPos - fruits[j][0]
                b = fruits[i][0] - startPos
                if a <= 0:
                    d = b
                elif b <= 0:
                    d = a
                else:
                    d = min(a,b)*2 + max(a,b)
                if d <= k: break
                score -= fruits[j][1]
                j += 1
            res = max(res, score)
        return res