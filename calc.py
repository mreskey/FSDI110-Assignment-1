# description
"""
PyCalc: Simple calculator
Author: Mark Eskey
Date: 6/14/21
Functionality:
    - Simple mathematical operations (sum, subtraction, multiplication, division)
"""


# imports


# globals


# function


def print_menu():
    print("------------------")
    print("Welcome to PyCalc")
    print("------------------")
    print("1 - Sum")
    print("2 - Subtract")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Is it odd?")
    print("6 - Print a message N times")
    print("q - Quit")
    print("------------------")


def clear():
    print("\n\n\n\n\n")


def print_result():
    print(f"The result is: {ans}")


# instructions
selected_option = ""

while(selected_option != "q"):
    clear()
    print_menu()

    selected_option = input("Select an option: ")

    if selected_option == "q":
        break

    elif selected_option == "1":
        num_1 = input("Input first number: ")
        num_2 = input("Input second number: ")
        ans = float(num_1) + float(num_2)
        print_result()

    elif selected_option == "2":
        num_1 = input("Input first number: ")
        num_2 = input("Input second number: ")
        ans = float(num_1) - float(num_2)
        print_result()

    elif selected_option == "3":
        num_1 = input("Input first number: ")
        num_2 = input("Input second number: ")
        ans = float(num_1) * float(num_2)
        print_result()

    elif selected_option == "4":
        num_1 = input("Input first number: ")
        num_2 = input("Input second number: ")
        if num_2 != "0":
            ans = float(num_1) / float(num_2)
            print_result()
        else:
            print("Error, cannot divide by 0.")

    elif selected_option == "5":
        num_1 = input("Input your number: ")
        remainder = int(num_1) % 2
        if remainder == 0:
            print("The number is even.")
        else:
            print("The number is odd.")

    elif selected_option == "6":
        message = input("Input your message: ")
        n = input("How many times would you like to repeat your message?: ")
        i = 0
        while i < int(n):
            print(message)
            i += 1

    else:
        print("Please select a valid operation.")

    input("\nPress enter to continue...")

print("Goodbye!")
