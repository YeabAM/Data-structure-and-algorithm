if __name__ == '__main__':
    student=[]
    secondLeast=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
        results=[student[i][1] for i in range (len(student))]
    minimum=min(results)
    for i in range(len(results)):
        if(min(results)==minimum):
            results.remove(min(results))
            
    minimum=min(results)
    for i in range(len(student)):
         if student[i][1]==minimum:
            secondLeast.append(student[i][0])
    secondLeast.sort()
    for i in range(len(secondLeast)):
        print(secondLeast[i])
