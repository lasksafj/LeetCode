class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def f(s):
            s = s.split('-')
            m,d = int(s[0]), int(s[1])
            A = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return sum(A[:m-1]) + d
        a1,a2 = f(arriveAlice), f(leaveAlice)
        b1,b2 = f(arriveBob), f(leaveBob)
        return max(0, min(a2,b2)+1 - max(a1,b1))