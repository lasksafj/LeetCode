class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        c1 = Counter(secret)
        c2 = Counter(guess)
        b = 0
        for n in c1:
            b += min(c1[n], c2[n])
        a = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
        b -= a
        return str(a) + 'A' + str(b) + 'B'