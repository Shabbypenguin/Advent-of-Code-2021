with open("problem-1-input.txt") as file:
    oldLine1 = 0
    oldLine2 = 0
    oldLine3 = 0
    increased = 0
    for line in file:
        if (int(oldLine1)+int(oldLine2)+int(line)) > (int(oldLine3)+int(oldLine2)+int(oldLine1)):
            print(line)
            if oldLine3 != 0:
                print((int(oldLine1)+int(oldLine2)+int(line)))
                increased +=1
        oldLine3 = oldLine2
        oldLine2 = oldLine1
        oldLine1 = line
    print(increased)