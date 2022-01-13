# Enter your code here. Read input from STDIN. Print output to STDOUT
cases=int(input())
for i in range(cases):
    a,b = input().split()
    try:
        print (int(a)//int(b))
    except (ZeroDivisionError , ValueError) as e:
        print('Error Code: ' + str(e))

