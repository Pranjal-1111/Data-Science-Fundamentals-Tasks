# numbers.py

# Ask the user to enter three different integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate and print the required results
sum_of_numbers = num1 + num2 + num3
difference_of_first_two = num1 - num2
product_of_first_and_third = num1 * num3
sum_divided_by_third = (num1 + num2 + num3) / num3

print(f"The sum of all the numbers: {sum_of_numbers}")
print(f"The first number minus the second number: {difference_of_first_two}")
print(f"The third number multiplied by the first number: {product_of_first_and_third}")
print(f"The sum of all three numbers divided by the third number: {sum_divided_by_third}")
