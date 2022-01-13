# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
nums = input().split()
print(all([int(x) > 0 for x in nums]) and any(" ".join(reversed(i)) == i for i in nums))
