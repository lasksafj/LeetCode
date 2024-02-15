from sortedcontainers import SortedList

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        B = initialBoxes.copy()
        K = SortedList()
        done = False
        res = 0
        while not done:
            done = True
            # print(B,K)
            i = len(B) - 1
            while i >= 0:
                # print('--',i,B)
                b = B[i]
                if status[b] == 0:
                    p = K.bisect_left(b)
                    if p == len(K) or K[p] != b:
                        i -= 1
                        continue
                    K.discard(b)
                    # print('----',p,K)
                B[i],B[-1] = B[-1],B[i]
                B.pop()
                res += candies[b]
                for nb in containedBoxes[b]:
                    B.append(nb)
                for k in keys[b]:
                    K.add(k)
                done = False
                i -= 1
            
        return res