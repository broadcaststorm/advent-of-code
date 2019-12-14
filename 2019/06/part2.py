#!/usr/bin/env python3

from part1 import build_bodies


def build_path(bodies, moon):
    """
    Return a list of bodies the moon is orbiting back to COM
    """

    path = []

    body = moon.parent
    while(body is not None):
        path.insert(0, body.value)
        body = body.parent

    return path


if __name__ == '__main__':

    with open('part1.txt', 'r') as f:
        entries = f.readlines()

    bodies = build_bodies(entries)

    you = bodies['YOU']
    my_path = build_path(bodies, you)
    print(my_path)

    santa = bodies['SAN']
    santa_path = build_path(bodies, santa)
    print(santa_path)

    # Our orbits will share a comment root so find the point of divergence
    common = 0
    while (my_path[common] == santa_path[common]):
        common = common + 1

    # Back up the pointer to the last matching orbit
    common = common - 1

    # len() is my location, len()-1 is my orbit
    down_orbit = (len(my_path) - 1) - common
    up_orbit = (len(santa_path) - 1) - common

    print(down_orbit, up_orbit)
    print('Orbit transitions is {0}'.format(down_orbit+up_orbit))
