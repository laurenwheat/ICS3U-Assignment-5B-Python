#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program displays the LCM of 2 numbers

def main():

    a = input("Please enter the first value: ")
    b = input("Please enter the second value: ")

    try:
        a_int = int(a)
        b_int = int(b)

        if (a_int > b_int):
            maximum = a_int
        else:
            maximum = b_int

        while(True):
            if(maximum % a_int == 0 and maximum % b_int == 0):
                print("LCM is {0}".format(maximum))
                break
            maximum = maximum + 1
    
    except Exception:
        print("That is not a number!!!!!!")
    finally:
        print("")
        print("Thanks for playing <3")


if __name__ == "__main__":
    main()
