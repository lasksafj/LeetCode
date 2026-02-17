class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        T = [0,1,2,3]
        B = [0,1,2,3,4,5]
        for t in range(min(turnedOn, 4) + 1):
            top = []
            for comb in combinations(T, t):
                x = 0
                for d in comb:
                    x |= 1<<d
                if 0 <= x < 12:
                    top.append(x)
            b = turnedOn - t
            bot = []
            for comb in combinations(B, b):
                x = 0
                for d in comb:
                    x |= 1<<d
                if 0 <= x < 60:
                    bot.append(x)
            for t in top:
                for b in bot:
                    res.append(str(t) + ':' + str(b).zfill(2))
        return res