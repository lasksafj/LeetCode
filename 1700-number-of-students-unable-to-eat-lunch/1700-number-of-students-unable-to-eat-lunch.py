class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = sandwiches[::-1]
        while students:
            i = 0
            while i < len(students) and students[0] != sandwiches[-1]:
                students.append(students.popleft())
                i += 1
            if i == len(students):
                return len(students)
            students.popleft()
            sandwiches.pop()
        return 0