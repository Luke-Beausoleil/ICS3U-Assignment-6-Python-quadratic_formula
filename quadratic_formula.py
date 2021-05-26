#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program evaluates the quadratic formula with user inputs

import math


def discriminant(a, b, c):
    discriminant_value = (b ** 2) - (4 * a * c)

    return discriminant_value


def value1(a, b, c):
    # this function evaluates the first root
    first_root = ((-1 * b) + math.sqrt(discriminant(a, b, c))) / (2 * a)

    return first_root


def value2(a, b, c):
    # this function evaluates the second root
    second_root = ((-1 * b) - math.sqrt(discriminant(a, b, c))) / (2 * a)

    return second_root


def main():
    # this function receives input and calls another function

    # input
    print("Given the standard formula: 0 = ax² + bx + c")
    a_string = input("Enter the value for 'a': ")
    b_string = input("Enter the value for 'b': ")
    c_string = input("Enter the value for 'c': ")
    try:
        a = float(a_string)
        b = float(b_string)
        c = float(c_string)
        if discriminant(a, b, c) < 0:
            print("No roots\nDone.")
        elif discriminant(a, b, c) == 0:
            x1 = value1(a, b, c)
            print("x = {0}".format(x1))
        else:
            x1 = value1(a, b, c)
            x2 = value2(a, b, c)
            print("x = {0}\nx = {1}\nDone.".format(x1, x2))
    except(Exception):
        print("Invalid Input.\nDone.")


if __name__ == "__main__":
    main()
