class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        res = 0
        for a in range(1,27):
            l = a*k
            if l > len(word):
                return res
            j = 0
            i = 0
            m = [0]*26
            no_ch = 0
            while j < len(word):
                ch_j = ord(word[j]) - ord('a')
                m[ch_j] += 1
                if m[ch_j] == 1:
                    no_ch += 1
                while j-i+1 > l or m[ch_j] > k:
                    ch_i = ord(word[i]) - ord('a')
                    m[ch_i] -= 1
                    if m[ch_i] == 0:
                        no_ch -= 1
                    i += 1
                if j == 0 or l == 1 or (abs(ord(word[j]) - ord(word[j-1])) <= 2):
                    if j-i+1 == l and no_ch == a:
                        res += 1
                        # print(a,i,j,word[j],m[word[j]])
                else:
                    i = j
                    m = [0]*26
                    m[ch_j] += 1
                    no_ch = 1
                j += 1
        return res