class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        for i in range(len(students)):
            if cnt[sandwiches[i]]:
                cnt[sandwiches[i]] -= 1
            else:
                return sum(b for b in cnt.values())
        return 0