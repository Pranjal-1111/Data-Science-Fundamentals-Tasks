# Write Python code to take the name of a user's favourite restaurant
string_fav = input("Enter your favorite restaurant: ")

# Take in the user's favourite number and use casting to store it in an integer variable called int_fav
int_fav = int(input("Enter your favorite number: "))

# Print out the user's favorite restaurant and favorite number using two separate print statements
print("Your favorite restaurant is:", string_fav)
print("Your favorite number is:", int_fav)

# Try to cast string_fav to an integer and add a comment to explain the result
try:
    int_string_fav = int(string_fav)
except ValueError as e:
    print(f"Error: {e}. Cannot cast {string_fav} to an integer.")
    # Explanation: If the user entered a non-numeric value for their favorite restaurant,
    # the int() function will raise a ValueError since it cannot convert a non-numeric string to an integer.
