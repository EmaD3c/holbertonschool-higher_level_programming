#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # Capturer les exceptions si la valeur n'est pas un entier
        return False
