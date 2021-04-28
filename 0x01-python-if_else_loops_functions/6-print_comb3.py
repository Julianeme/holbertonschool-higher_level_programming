#!/usr/bin/python3
uinit = 1
for x in range(0, 10):
    for y in range(uinit, 10):
        print("{:d}{:d}" .format(x, y), end="")
        if ((x == 8) and (y == 9)):
            print()
        else:
            print(", ", end="")
    uinit = uinit + 1
