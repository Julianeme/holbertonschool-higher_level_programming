#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenght = len(sys.argv)
    if lenght == 1:
        print("0 arguments.")
    elif lenght == 2:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    elif lenght > 2:
        print("{} arguments:".format(lenght - 1))
        for x in range(1, len(sys.argv)):
            print("{}: {}".format(x, sys.argv[x]))
