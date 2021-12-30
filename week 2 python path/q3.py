row = 4
space = 6
stars = 1
for i in range(row):
    print("*" * stars,end="")
    print(" " * space,end="")
    print("*" * stars,end="")
    print(" ")
    stars += 1
    space -= 2
    
    
    