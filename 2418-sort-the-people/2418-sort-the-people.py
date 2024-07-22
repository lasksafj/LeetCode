class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [names[i] for i in sorted(list(range(len(names))), key=lambda i:-heights[i])]