class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        N = len(colors)
        ra,rb = 0,0
        i,j = 0,0
        while i < N:
            j = i+1
            while j < N and colors[j] == colors[i]:
                j += 1
            if colors[i] == 'A':
                ra += max(0, j-i-2)
            else:
                rb += max(0, j-i-2)
            i = j
            print(ra,rb)
        return ra > rb