class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        N = len(word)
        l = N-numFriends+1
        i,j = 0,1
        k = 0
        while j+k < N:
            if word[i+k] == word[j+k]:
                k += 1
            elif word[i+k] < word[j+k]:
                i = max(i+k+1, j)
                j = i+1
                k = 0
            else:
                j += k+1
                k = 0
        return word[i:][:l]