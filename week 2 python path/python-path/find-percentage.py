if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    average=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        marks=student_marks[query_name]
    for i in marks:
        average=average+i
    average=float(average/3)
    print("%.2f" % average)
