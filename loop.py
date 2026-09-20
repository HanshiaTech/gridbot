ccfile = open("symbols.txt", "r")

for aline in ccfile:
    values = aline.split()
    print( values[0])

ccfile.close()
