def do_pattern(H):
    space = H
    for i in range(1, H+3):       
        if i %2 == 0:
            for j in range(H-1):
                print(" ",end=" ")
                print("#" * (H-1),end=" ")            
        else:
            for j in range(H):
                print("#" * (H-1),end="  ")                 
        print(" ")