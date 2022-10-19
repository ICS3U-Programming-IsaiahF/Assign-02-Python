#!/usr/bin/env python3

# Created by: Isaiah Fernandez
# Date: October 11, 2022
# This program calculates the area and perimeter pf a rhombus with user input.

import math

# This function gets user input for side length and one diameter of rhombus.
side_rhombus = float(input("What is the side length of the rhombus in cm? "))
diam_one = float(input("What is the length of one diagonal of the rhombus in cm? "))


def main():
    a_or_p = input("Are you looking to solve for area (a) or perimeter (p):")

    if a_or_p == "a":

        # This function calculates the area of the rhombus.
        diam_two_sq = float(side_rhombus**2 - ((diam_one / 2) ** 2))
        diam_two = 2 * (math.sqrt(diam_two_sq))
        area_rhombus = (diam_one * diam_two) * 1 / 2
        print("The area of the rhombus is {:.2f}cm^2".format(area_rhombus))

    elif a_or_p == "p":
        perim_rhombus = side_rhombus * 4
        print("The perimeter of the rhombus is {:.2f}cm".format(perim_rhombus))

    else:
        print("please enter a or p for area or perimeter")


if __name__ == "__main__":
    main()
