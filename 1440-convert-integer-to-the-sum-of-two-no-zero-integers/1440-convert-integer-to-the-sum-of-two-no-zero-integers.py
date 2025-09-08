class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a,b = 0,0
        tens = 1
        while n:
            n,d = divmod(n,10)
            if d == 0:
                a += 5*tens
                b += 5*tens
                n -= 1
            elif d == 1 and n >= 1:
                a += 6*tens
                b += 5*tens
                n -= 1
            else:
                a += 1*tens
                b += (d-1)*tens
            tens *= 10
        return [a,b]