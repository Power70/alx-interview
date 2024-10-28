#!/usr/bin/python3
"""
This module contains the function validUTF8
to validate if a data, conforms to the UTF-8 encoding.
"""


def validUTF8(data):
    "Determine if a given data set represents a valid UTF-8 encoding"
    # Initialize index i to 0
    i = 0
    # While there are still bytes to check in the data
    while i < len(data):
        # Read the current byte
        byte = data[i] & 0xFF
        # Determine the number of bytes in the character
        #  based on the first byte
        if (byte & 0b10000000) == 0:
            # Single-byte character (ASCII)
            num_bytes = 1
        elif (byte & 0b11100000) == 0b11000000:
            # Two-byte character
            num_bytes = 2
        elif (byte & 0b11110000) == 0b11100000:
            # Three-byte character
            num_bytes = 3
        elif (byte & 0b11111000) == 0b11110000:
            # Four-byte character
            num_bytes = 4
        else:
            # Invalid leading byte
            return False

        # Check that the following bytes are valid continuation bytes
        for j in range(1, (num_bytes)):
            # Move to the next byte
            i += 1
            # Check if the next byte exists
            # and is a valid continuation byte (starts with 10xxxxxx)
            if i >= len(data) or ((data[i] & 0b11000000) != 0b10000000):
                return False

        # Move to the next character in the data
        i += 1

    # All bytes were valid
    return True
