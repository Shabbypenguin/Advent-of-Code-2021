import re

with open("day-2-input.txt") as file:
    depth = 0
    horizontal = 0
    aim = 0
    for line in file:
        if re.search("up", line):
            change = re.findall(r'[0-9]{1,}', line)
            print("going up " + change[0])
            aim = aim - int(change[0])
        elif re.search("down", line):
            change = re.findall(r'[0-9]{1,}', line)
            print("going down " + change[0])
            aim = aim + int(change[0])
        elif re.search("forward", line):
            change = re.findall(r'[0-9]{1,}', line)
            print("Going forward " + change[0])
            horizontal = horizontal + int(change[0])
            depth = depth + (aim*int(change[0]))
    print(depth)
    print(horizontal)
    print(int(depth)*int(horizontal))
