row = 4
space = row
stars = 1
for i in range(row):
    print(" " * space,end="")
    print("*" * stars)
    stars += 2
    space -= 1
    
    
    