##
# @file stddev.py
# @brief Standard deviation calculation for IVS Project 2
# @author Marek Antoňů (xanton07)
# @date April 2023

import mathlib as math
import sys


def main():
    arr = list()

    # loading input to list
    while True:
        try:
            arr.extend(list(map(float, input().split())))
        except EOFError:
            break
        except ValueError:
            print("Error: invalid value")
            sys.exit()

    # checking number of inputs
    size = len(arr)

    if size < 2:
        print("Error: at least two values must be entered")
        sys.exit()

    sum = 0
    avg = 0

    # calculating sum and average
    for i in arr:
        sum = math.addition(sum, math.power(i, 2))
        avg = math.addition(avg, i)

    # final calculations
    avg = math.power(math.division(avg, size), 2)
    avg = math.multiplication(size, avg)

    dev = math.division(math.subtraction(sum, avg), math.subtraction(size, 1))
    dev = math.root(2, dev)

    # printing result
    print(dev)


if __name__ == '__main__':
    main()
