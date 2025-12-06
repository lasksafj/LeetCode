class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        A = [0]*(length+1)
        for s,e,i in updates:
            A[s] += i
            A[e+1] -= i
        return list(accumulate(A))[:-1]