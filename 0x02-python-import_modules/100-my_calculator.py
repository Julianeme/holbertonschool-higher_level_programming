#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    import sys
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if len(sys.argv) != 4:
        print("print Usage: ./100-my_calculator.py <a> <operator> <b>")
    elif sys.argv[2] == chr(43):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sys.argv[2] == chr(45):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif sys.argv[2] == char(42):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif sys.argv[2] == char(47):
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
