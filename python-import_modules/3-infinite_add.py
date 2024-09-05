#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Initialize the sum variable
    total_sum = 0

    # Iterate over the arguments starting from index 1 to skip script name
    for arg in sys.argv[1:]:
        # Convert each argument to an integer and add it to the total
        total_sum += int(arg)

    # Print the result
    print(total_sum)
