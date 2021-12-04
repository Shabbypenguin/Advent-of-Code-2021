with open("problem-1-input.txt") as file:
    oldLine = 0
    increased = 0
    for line in file:
        if int(line) > int(oldLine):
            if oldLine != 0:
                print( line + " ")
                increased +=1
        oldLine = line
    print(increased)