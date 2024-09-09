#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        # Delete the element at the specified index using list slicing
        del my_list[idx]
    return my_list
