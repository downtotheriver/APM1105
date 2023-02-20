import math


# 1. Write a Python function to multiply all the numbers in a list.
def multiplication(samples):
    product = math.prod(samples)
    print("1. The product of", samples, "is", product, end=".")


samples = [5, 6, -1, 2, 4, -2, -10, 7]
multiplication(samples)


# 2. Write a function that draws a grid like the following:
def grid():
    print("+ - - - - + - - - - + - - - - + - - - - +")
    for loop in range(1,5):
        print("|         |         |         |         |")
        print("|         |         |         |         |")
        print("|         |         |         |         |")
        print("|         |         |         |         |")
        print("+ - - - - + - - - - + - - - - + - - - - +")


print("\n\n2. Grid:")
grid()

# User input for number 1
def multiplication(numbers_list):
    product = math.prod(numbers_list)
    print("1. The product of", numbers_list, "is", product, end=".")


print("\nUSER INPUT FOR NUMBER 1")
numbers_list = list(map(float, input("Enter the numbers separated by space: ").split()))
multiplication(numbers_list)
