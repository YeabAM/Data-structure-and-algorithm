class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        income = dict()
        preqs = defaultdict(list)
        queue = deque()
        courses = []
        for c in range(numCourses):
            income[c] = 0

        for cour, pre in prerequisites:
            preqs[pre].append(cour)
            income[cour] += 1

        for cour in income:
            if income[cour] == 0:
                queue.append(cour)

        while queue:
            curr = queue.popleft()
            courses.append(curr)
            for cour in preqs[curr]:
                income[cour] -= 1
                if income[cour] == 0:
                    queue.append(cour)

        if len(income) == len(courses):
            return courses
        return []
        