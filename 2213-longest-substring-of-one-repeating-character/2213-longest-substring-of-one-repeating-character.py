from sortedcontainers import SortedList

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        N = len(s)
        mp = defaultdict(SortedList)
        i = 0
        res = []
        B = SortedList()
        while i < N:
            j = i+1
            while j < N and s[j] == s[i]:
                j += 1
            mp[s[i]].add([i,j])
            B.add(j-i)
            i = j
        s = [ch for ch in s]
        for ch,i in zip(queryCharacters,queryIndices):
            o_ch = s[i]
            if o_ch == ch:
                res.append(B[-1])
                continue
            s[i] = ch
            A = mp[ch]
            if len(A) == 0:
                A.add([i,i+1])
                B.add(1)
            else:
                p = A.bisect_right([i,inf])
                if p == 0:
                    if A[p][0] == i+1:
                        B.discard(A[p][1] - A[p][0])
                        A[p][0] = i
                        B.add(A[p][1] - A[p][0])
                    else:
                        A.add([i,i+1])
                        B.add(1)
                elif p == len(A):
                    if A[p-1][1] == i:
                        B.discard(A[p-1][1] - A[p-1][0])
                        A[p-1][1] = i+1
                        B.add(A[p-1][1] - A[p-1][0])
                    else:
                        A.add([i,i+1])
                        B.add(1)
                else:
                    if A[p-1][1] < i and A[p][0] > i+1:
                        A.add([i,i+1])
                        B.add(1)
                    elif A[p-1][1] == i and A[p][0] == i+1:
                        B.discard(A[p][1] - A[p][0])
                        B.discard(A[p-1][1] - A[p-1][0])
                        A[p-1][1] = A[p][1]
                        A.discard(A[p])
                        B.add(A[p-1][1] - A[p-1][0])
                    elif A[p-1][1] == i:
                        B.discard(A[p-1][1] - A[p-1][0])
                        A[p-1][1] = i+1
                        B.add(A[p-1][1] - A[p-1][0])
                    else:
                        B.discard(A[p][1] - A[p][0])
                        A[p][0] = i
                        B.add(A[p][1] - A[p][0])
            # print(ch,A)
            
            A = mp[o_ch]
            p = A.bisect_right([i,inf])
            p -= 1
            l,r = A[p]
            B.discard(r-l)
            if r - l == 1:
                A.discard(A[p])
            elif l == i:
                A[p][0] = i+1
                B.add(r-l-1)
            elif A[p][1] == i+1:
                A[p][1] = i
                B.add(r-l-1)
            else:
                A[p][1] = i
                A.add([i+1,r])
                B.add(i-l)
                B.add(r-(i+1))
            # print(o_ch,A)
            # print(B)
            
            res.append(B[-1])
            
        return res
        