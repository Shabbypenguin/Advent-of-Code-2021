i = 0
bigdigit = []
smalldigit = []

def read_lines(i):
    with open("Day-3-input.txt") as file:
        zerocounter = 0
        onecounter = 0
        for line in file:
            if line[i] == "0":
                zerocounter += 1
            elif line[i] == "1":
                onecounter +=1
        if zerocounter > onecounter:
            bigdigit.append(0)
        elif zerocounter < onecounter:
            bigdigit.append(1)
        if zerocounter < onecounter:
            smalldigit.append(0)
        elif zerocounter > onecounter:
            smalldigit.append(1)



while i < 12:
    read_lines(i)
    i += 1

print("\ngamma rate is: ")
bigdigitlist = ''.join(map(str, bigdigit))
print(bigdigitlist)
bigdigitlistdec = int(bigdigitlist, 2)
print("Decimal form: " + str(bigdigitlistdec))
print("\nepsilon rate is: ")
smalldigitlist = ''.join(map(str, smalldigit))
print(smalldigitlist)
smalldigitlistdec = int(smalldigitlist, 2)
print("Decimal form: " + str(smalldigitlistdec))
print("\npower consumption is: ")
print(smalldigitlistdec*bigdigitlistdec)



