#!/usr/bin/python3

# Runs the code below only if this file is executed directly, not when imported
if __name__ == "__main__":
    from add_0 import add
    # Assign the values to variables a and b
    a = 1
    b = 2
    # Print the result using string formatting
    print("{} + {} = {}".format(a, b, add(a, b)))
