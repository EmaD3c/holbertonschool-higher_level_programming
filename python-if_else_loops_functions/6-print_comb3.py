#!/usr/bin/python3

# Loop through the first digit from 0 to 8
for num1 in range(0, 9):
    # Loop through the second digit from num1 + 1 to 9
    for num2 in range(num1 + 1, 10):
        # Print the last pair without a trailing comma
        if (num1 == 8 and num2 == 9):
            print("{}{}".format(num1, num2))
        # Print other pairs with a comma and space
        else:
            print("{}{}".format(num1, num2), end=", ")
