#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # len(my_list) - 1 gives the index of the last element in the list
    # The second -1 to stop the iteration just before reaching this value
    # The third -1 to decrement the index each time, so we move backwards
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
