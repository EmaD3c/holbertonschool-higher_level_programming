#!/usr/bin/python3
def number_keys(a_dictionary):
  count = 0
    for key in test_dict:
        count += 1
        if isinstance(test_dict[key], dict):
            count += number_keys(test_dict[key])
    return count