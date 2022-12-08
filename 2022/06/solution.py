#!/usr/bin/env python3
"""
2022/06/solution.py: Python based solution to Day 6

Given the slightly different nature of the problem setup, I'm going to use
that main body to open the input file and slurp in the string.  This allows
me to simply use part1 and part2 as unit tests were I pass multiple strings
provided by the problem setup.
"""


def part1(stream_buffer: str, sync_window: int = 4) -> int:
    """
    part1(stream_buffer, sync_window) - give a signal stream buffer and a
    search window of size 'sync_window', search for the first occurrence
    of a unique set of characters within that sync_window, returning the
    index of the last character seen (counting the buffer from 1!!!).

    As such, the "smallest" result that could be returned is sync_window.
    """

    # Determine size of the incoming stream buffer
    buffer_size = len(stream_buffer)

    # Current starting position is the end of a sync_window
    marker = sync_window

    # Walk through the stream buffer
    while marker <= buffer_size:
        # For the sync_window sub-string, convert to a set to find
        # all the unique characters in this sync_window
        test_window = set(stream_buffer[marker-sync_window:marker])

        # if I have duplicates, the set size will be smaller than sync_window
        if len(test_window) == sync_window:
            return marker

        # Keep marching on
        marker += 1


def part2(stream_buffer: str, start_marker: int = 1) -> int:
    """
    part2(stream_buffer, starting point) - the start of message requirement in
    the problem requires looking for unique string of characters in a 14 char
    sync window.

    Originally, I thought this would be AFTER the start of signal sync (hence)
    the start_marker option. However, based on the answers, apparently not.
    Hence the start_marker reset to 1, hard coded here.
    """

    start_marker = 1
    return part1(stream_buffer[start_marker-1:], sync_window=14)


if __name__ == '__main__':

    # Solve part1
    with open(file='input-part1.txt', mode='r', encoding='UTF-8') as f_obj:
        input_stream = f_obj.read().strip()

    result = part1(input_stream)
    print(f'Result is {result}')

    # Solve part2
    output = part2(input_stream, result)
    print(f'Output is {output}')
