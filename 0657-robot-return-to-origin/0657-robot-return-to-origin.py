class Solution:
    def judgeCircle(self, moves: str) -> bool:
        mp = Counter(moves)
        return mp['U'] == mp['D'] and mp['L'] == mp['R']