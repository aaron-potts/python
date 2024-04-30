# number_1 = int(input("Enter the first number: "))
# number_2 = int(input("Enter the second number: "))
# print(f"{number_1} * {number_2} = {number_1 * number_2}")

def multiply(left, right):
    return left * right

def get_number(prompt):
    num = float(input(prompt))
    return num

first = get_number("Enter the first number: ")
second = get_number("Enter the second number: ")
print(f"{first} * {second} = {multiply(first, second)}")