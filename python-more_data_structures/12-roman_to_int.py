#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0  # Return 0 if input is invalid

    # Define Roman numeral values
    romannb = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0

    # Loop through the Roman numeral string in reverse
    for char in reversed(roman_string):
        value = romannb.get(char, 0)
        if value >= prev_value:
            # Add if it's larger or equal to the previous value
            total += value
        else:
            # Subtract if it's smaller (subtractive notation)
            total -= value
        prev_value = value

    return total
