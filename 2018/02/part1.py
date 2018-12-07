#!/usr/bin/env python3
"""
Find strings that have characters that are replicated either exactly 2 
or exactly 3 (or both) times.  Use the count of box IDs matching those
requirements to calculate a checksum (num_two * num_three).

General approach - loop over each character in the box ID string and 
use the re.findall method to return a list of matches to that character
and simply use the length of the list.
"""
import re


# If this code is being executed, rather than imported
if __name__ == '__main__':

    num_two = 0
    num_three = 0

    # Open the file as 'f'
    with open('input.txt', 'r') as f:

        # Read each line into 'l'
        for l in f:

            has_two = False
            has_three = False

            # Loop over each character c
            for c in l:

                # Find all c in the string
                result = re.findall(c, l)

                # If we found 2 or 3 c in l, flag success
                if len(result) == 2:
                    has_two = True
                if len(result) == 3:
                    has_three = True

                # If we've found both, go ahead and exit
                if has_two and has_three:
                    break

            if has_two:
                num_two = num_two + 1

            if has_three:
                num_three = num_three + 1

    # Now that we've read the entire file, generate the checksum
    checksum = num_two * num_three
    print('Checksum is {} * {} = {}'.format(num_two, num_three, checksum))
