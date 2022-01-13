# Enter your code here. Read input from STDIN. Print output to STDOUT
std,sbj = input().split()
subject=list()
Sum=0
for i in range(int(sbj)):
    subject.append(list(map(float,input().split())))
subject=list((zip(*subject)))
for z in range(int(std)):
    Sum=sum(subject[z])
    print(float(Sum/float(sbj)))
