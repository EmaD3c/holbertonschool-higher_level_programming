#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # Apply the map with the correct lambda function using the provided number
    my_new_list = list(map(lambda x: x * number, my_list))
    return my_new_list
