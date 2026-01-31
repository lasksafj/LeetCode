class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        a = letters[0]
        letters.sort()
        i = bisect_right(letters, target)
        return letters[i] if i < len(letters) else a