import Constants


def simple_calculator():
        print("Enter 1 number:", end=" ")
        num1 = int(input())
        print("Enter 2 number:", end=" ")
        num2 = int(input())
        print("Enter operation what are you gonna to do:", end=" ")
        operation = str.lower(input())
        print("Result:", end=" ")
        if operation == Constants.CONSTANTS_OPERATIONS["Add"]:
                return num1 + num2
        elif operation == Constants.CONSTANTS_OPERATIONS["Sub"]:
                return num1 - num2
        elif operation == Constants.CONSTANTS_OPERATIONS["Mul"]:
                return num1 * num2
        elif operation == Constants.CONSTANTS_OPERATIONS["Div"] and num2 != 0:
                return num1 / num2
        else: print("Error! Try again! ", end="")


