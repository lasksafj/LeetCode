class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m,n = len(word1),len(word2)
        i,j = m-1,n-1
        cover = [n]*(m+1)
        while i >= 0:
            if j >= 0 and word1[i] == word2[j]:
                cover[i] = j
                j -= 1
            else:
                cover[i] = cover[i+1]
            i -= 1
        i,j = 0,0
        res = []
        while i < m and j < n:
            if word1[i] == word2[j]:
                res.append(i)
                i += 1
                j += 1
            else:
                if cover[i+1] <= j+1:
                    res.append(i)
                    i += 1
                    j += 1
                    break
                else:
                    i += 1
        while i < m and j < n:
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            i += 1
        return res if len(res) == n else []