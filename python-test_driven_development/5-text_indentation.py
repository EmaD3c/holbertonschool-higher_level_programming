#!/usr/bin/python3
"""Defines text_indentation function."""


def text_indentation(text):
    """
    Prints a text with 2 newlines
    after each of the following characters: '.', '?' and ':'.

    Args:
    text (str): The text to be processed and printed.

    Raises:
    TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    specChar = {'.', '?', ':'}
    start = 0
    length = len(text)

    while start < length:
        end = start

        # Find the end of the current segment
        while end < length and text[end] not in specChar:
            end += 1

        # Print the segment with added newlines if it's followed by a delimiter
        if end < length and text[end] in specChar:
            # Include the delimiter in the segment
            end += 1
            # Print the segment and add two newlines
            print(text[start:end].strip() + "\n\n", end="")
            # Move start to the next character after the delimiter
            start = end
        else:
            # Print the remaining part of the text
            print(text[start:].strip(), end="")
            break
