def rom_to_int(rom):
    sum = 0
    romans = { "I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000         
             }
    for i in range(len(rom)):

        if i < (len(rom) - 1) and romans[rom[i]] < romans[rom[i+1]]:
            sum -= romans[rom[i]]  
        else:
            sum += romans[rom[i]]
    print(sum)