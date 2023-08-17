class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        i,j = 0, len(s)-1
        A = list(s)
        res = 0
        while A:
            # print(A)
            i = A.index(A[-1])
            if i < len(A)-1:
                res += i
                A.pop(i)
            else:
                res += i//2
            if A:
                A.pop()
            # print(res)
        return res