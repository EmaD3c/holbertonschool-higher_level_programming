#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new empty list to store the result
    new_list = []

    # Loop through each element in the original list
    for element in my_list:
        # If the element matches the search value, add the replace value
        if element == search:
            new_list.append(replace)
        else:
            # Otherwise, add the element as it is
            new_list.append(element)

    # Return the new list
    return new_list
