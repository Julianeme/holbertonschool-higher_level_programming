#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    lenght = len(sys.argv)
    num_arg = len(sys.argv)
    if lenght == 1:
        print("0")
    elif lenght == 2:
        print("{}".format(int(sys.argv[1])))
    elif lenght > 2:
        for x in range(1, len(sys.argv)):
            sum = sum + int(sys.argv[x])
        print("{}".format(sum))
