class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        for A in permutations(digits, 3):
            if A[0] == 0:
                continue
            n = 0
            for a in A:
                n = n*10 + a
            if n%2 == 0:
                res.add(n)
        return sorted(res)