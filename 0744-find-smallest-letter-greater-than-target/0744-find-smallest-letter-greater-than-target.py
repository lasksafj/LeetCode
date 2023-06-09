class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        p = bisect_right(letters, target)
        return letters[p] if p < len(letters) else letters[0]