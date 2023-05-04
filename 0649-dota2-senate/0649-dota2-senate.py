class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s = list(senate)
        br,bd = 0,0
        while 1:
            nr,nd = 0,0
            for i in range(len(s)):
                if s[i] == 'R':
                    if br == 0:
                        bd += 1
                        nr += 1
                    else:
                        br -= 1
                        s[i] = '-'
                elif s[i] == 'D':
                    if bd == 0:
                        br += 1
                        nd += 1
                    else:
                        bd -= 1
                        s[i] = '-'
            if nr == 0:
                return 'Dire'
            if nd == 0:
                return 'Radiant'
        return ''
            