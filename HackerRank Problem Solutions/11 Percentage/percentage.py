if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    avg = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks[query_name]:
        avg+=i
    print("{0:0.2f}".format(avg / len(student_marks[query_name])))