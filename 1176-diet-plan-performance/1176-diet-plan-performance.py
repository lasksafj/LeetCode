class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        cal = sum(calories[:k])
        res = 0
        if cal < lower: res -= 1
        if cal > upper: res += 1
        for i in range(k ,len(calories)):
            cal += calories[i] - calories[i-k]
            if cal < lower: res -= 1
            if cal > upper: res += 1
        return res