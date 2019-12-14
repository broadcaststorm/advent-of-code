#!/usr/bin/env python3
"""
day6: part1.py - pretty clear when need a tree data structure to represent
      the data.  Building a Node class with the parent (only one) and the
      children (possibly more than one).

      Also building a dictionary of all heavenly bodies so that I can locate
      one easily and then walk the path to COM via parent links/pointers or
      discover children via children array.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add(self, child):
        self.children.append(child)
        child.parent = self


def print_tree(bodies, top='COM', indent=''):
    root = bodies[top]
    print('{0}:{1}'.format(indent, top), len(root.children))
    i = 0
    for k in root.children:
        i = i + 1
        print_tree(bodies, top=k.value, indent=i)


def count_orbits(bodies):
    # Count the orbits
    orbits = 0

    for b in bodies:
        p = bodies[b].parent
        while(p is not None):
            orbits = orbits + 1
            p = p.parent

    return orbits


def build_bodies(entries):
    bodies = {}

    for entry in entries:
        body, moon = entry.rstrip().split(')')

        # We've not seen the parent body before
        if body not in bodies:
            b = Node(body)
            bodies[body] = b
        else:
            b = bodies[body]

        # We've not seen the moon before
        if moon not in bodies:
            m = Node(moon)
            bodies[moon] = m
        else:
            m = bodies[moon]

        b.add(m)

    return bodies


if __name__ == '__main__':

    with open('part1.txt', 'r') as f:
        entries = f.readlines()

    bodies = build_bodies(entries)

    orbits = count_orbits(bodies)
    print('Total direct and indirect orbits: {0}'.format(orbits))
