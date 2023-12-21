class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        A = [[n,int(t[:2])*60 + int(t[2:])] for n,t in access_times]
        A.sort()
        # print(A)
        res = []
        for i in range(len(A)):
            if res and res[-1] == A[i][0]:
                continue
            if i+2 < len(A):
                if A[i+2][0] == A[i][0] and A[i+2][1] - A[i][1] < 60:
                    res.append(A[i][0])
        return res