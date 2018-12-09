#!/usr/bin/env python3
"""
The general idea - use the concept of a histogram for tracking whether
the guard is asleep in the various minutes of the midnight hour.  In
parallel, also track - specifically for Puzzle 1 - the total number of
minutes asleep.

For this to make sense, the entire data set needs to be read in and
sorted.  Since the date/time is ISO format and ASCII sort friendly, each
line should be read in, regex'd into a datetime and status field, stored
as a key/value pair in a dictionary.

Once complete, the keys are extracted and sorted.  We can then pull the
sorted values by using the sorted keys.

There are a number of assumptions in this bugger:
 - Even though guards could start before midnight, they didn't fall
   asleep until after midnight
 - The data, once sorted, doesn't have logic issues (a guard doesn't
   wake up, even though he's already awake.  Go to sleep when he's
   already asleep)

My use of histogram concepts in puzzle 1 turned out to be fortuitous
for puzzle 2 (which you don't see ahead of time).  Hence, the two
puzzles are solved by the same program.

"""

import re


if __name__ == '__main__':

    # Whole line parsing
    pattern = r'\[(?P<datetime>\d\d\d\d\-\d\d\-\d\d \d\d:\d\d)\]'
    pattern = r'{} (?P<state>.*)\n'.format(pattern)
    parse = re.compile(pattern)

    # Date and time dissector
    pattern = r'(?P<year>\d\d\d\d)-(?P<month>\d\d)-(?P<day>\d\d)'
    pattern = r'{} (?P<hour>\d\d):(?P<min>\d\d)'.format(pattern)
    checkpoint = re.compile(pattern)

    # Extract guard information
    pattern = r'Guard #(?P<guard>\d+) begins shift'
    guard = re.compile(pattern)

    asleep = re.compile('falls asleep')
    awake = re.compile('wakes up')

    events = {}

    # read and parse all the input into something sortable
    with open('input.txt', 'r') as f:
        for l in f:
            result = parse.match(l)
            dt = result.group('datetime')
            state = result.group('state')

            events[dt] = state

    # Because we have ISO based date/time stamps, those values sort well
    sorted_events = sorted(events.keys())

    # Need to track total minutes asleep per guard
    guard_time = {}

    # Need to histogram minutes asleep per guard
    guard_minutes = {}

    # Initialize values
    id = 0
    last_min = 60
    last_day = '00-00'
    status = False

    # Loop through all events and track guard behavior
    for cp in sorted_events:
        # Extract the time stamp
        result = checkpoint.match(cp)
        this_day = '{}-{}'.format(result.group('month'), result.group('day'))
        this_min = int(result.group('min'))

        # Did we wake up?
        result = awake.match(events[cp])
        if result is not None:
            # Sanity check
            if not status:
                print("Guard woke up but not asleep")
                next

            # We wrapped to a new hour or day so handle it
            if (this_min < last_min) or (this_day != last_day):
                end = 60
            else:
                end = this_min

            # Record total times
            guard_time[id] = guard_time[id] + end - last_min

            # Record the minutes asleep
            for i in range(last_min, end):
                guard_minutes[id][i] = guard_minutes[id][i] + 1

            status = False

        # Did a guard start?
        result = guard.match(events[cp])
        if result is not None:
            id = int(result.group('guard'))
            status = False

            # Is this the first time we've seen this guard?
            if id not in guard_time:
                guard_time[id] = 0
            if id not in guard_minutes:
                guard_minutes[id] = [0]*60

        # Or did I go to sleep
        result = asleep.match(events[cp])
        if result is not None:
            status = True

        last_min = this_min
        last_day = this_day

    else:
        # After looping through all events, account for possibility
        # we were still asleep when our shift ended

        if status:
            # Record total times
            guard_time[id] = guard_time[id] + (60 - last_min)

            # Record the minutes asleep
            for i in range(last_min, 60):
                guard_minutes[id][i] = guard_minutes[id][i] + 1

    # Puzzle 1: Find the guard asleep the most, then the minute most asleep
    max_value = 0
    max_id = 0

    # Find the user with the most time asleep
    for id in guard_time.keys():
        if guard_time[id] > max_value:
            max_value = guard_time[id]
            max_id = id

    # For that user, find the time slot he was asleep the most in
    max_value = 0
    max_min = -1
    for min in range(0, 60):
        if guard_minutes[max_id][min] > max_value:
            max_min = min
            max_value = guard_minutes[max_id][min]

    print('Puzzle 1: {} {} {}'.format(max_id, max_min, max_id*max_min))

    # Puzzle 2: Find most frequent minute asleep, and the guard who slept it
    max_value = 0
    max_id = 0
    max_min = -1

    for id in guard_minutes.keys():
        for min in range(0, 60):
            if guard_minutes[id][min] > max_value:
                max_value = guard_minutes[id][min]
                max_id = id
                max_min = min

    print('Puzzle 2: {} {} {}'.format(max_id, max_min, max_id*max_min))
