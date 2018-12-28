#!/usr/bin/env python3
"""
Given the problem - the circle is represented by a list whose ever
increasing index (on the circle) is mapped to a finite list ranging from
0 to X by using the mod operator on the index value.

Solution to the both puzzles are provided by this same code.  Input
file has sample test cases from the problem definition as well as the
part1 and part2 inputs.
"""

import re
import datetime


def get_score(num_players, num_points):
    """
    Using a list to represent a circle.  After addition (clockwise) and
    subtraction (counter-clockwise), all indices must be 'mod'ed to
    ensure the index is within the range of the list.

    Marble values start at 1 and go to X points, so range() needs X+1
    """

    # Initialize circle
    circle = [0]
    current = 0

    # Initialize score
    score = [0]*num_players
    player = -1

    # Loop over all marbles
    for i in range(1, num_points+1):
        # Circumference of current circle
        n = len(circle)

        # Current player
        player = (player + 1) % num_players

        # Multiple of 23 behavior
        if i % 23 == 0:
            current = (current - 7) % n
            score[player] = score[player] + i + circle[current]
            circle.pop(current)
            continue

        # Insertion point of this marble
        current = (current + 1) % n + 1
        circle.insert(current, i)

        # For large iterations, let's keep track
        if i % 100000 == 0:
            t = datetime.datetime.now().isoformat()
            print('{} - Current i is {}'.format(t, i))

    # Find highest score
    max = 0
    for s in score:
        if s > max:
            max = s

    return max


if __name__ == '__main__':

    pattern = r'(?P<players>\d+) players;'
    pattern = r'{} last marble is worth (?P<points>\d+) points'.format(pattern)

    with open('input.txt', 'r') as f:
        for line in f:
            line.rstrip()

            result = re.match(pattern, line)
            num_players = int(result.group('players'))
            num_points = int(result.group('points'))

            score = get_score(num_players, num_points)
            print('{}: high score is {}'.format(result.group(), score))
            print(line)
