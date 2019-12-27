#!/usr/bin/env python3


import re

moon_names = ['Io', 'Europa', 'Ganymede', 'Callisto']


class Orbit:
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def apply_gravity(self, other):
        if self.x < other.x:
            self.vx = self.vx + 1
            other.vx = other.vx - 1
        elif self.x > other.x:
            self.vx = self.vx - 1
            other.vx = other.vx + 1

        if self.y < other.y:
            self.vy = self.vy + 1
            other.vy = other.vy - 1
        elif self.y > other.y:
            self.vy = self.vy - 1
            other.vy = other.vy + 1

        if self.z < other.z:
            self.vz = self.vz + 1
            other.vz = other.vz - 1
        elif self.z > other.z:
            self.vz = self.vz - 1
            other.vz = other.vz + 1

    def update_positions(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.z = self.z + self.vz

    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kinetic_energy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()


def report_kinematics(m):
    pos = 'pos=<x={0: 2}, y={1: 2}, z={2: 2}>'.format(m.x, m.y, m.z)
    vel = 'vel=<x={0: 2}, y={1: 2}, z={2: 2}>'.format(m.vx, m.vy, m.vz)
    print('{0}, {1}'.format(pos, vel))


def apply_time_step(moons):
    names = list(moons.keys())
    num_moons = len(names)

    for i in range(num_moons):
        me = moons[names[i]]
        for j in range(i+1, num_moons):
            you = moons[names[j]]
            me.apply_gravity(you)

    for i in range(num_moons):
        moons[names[i]].update_positions()


def extract_positions(filename='input.txt', obj=Orbit):
    pattern = re.compile(r'<x=(?P<x>.+?), y=(?P<y>.+?), z=(?P<z>.+?)>')

    orbits = list(moon_names)
    moons = {}
    with open(filename, 'r') as f:
        for position in f:
            result = pattern.match(position)
            x = int(result.group('x'))
            y = int(result.group('y'))
            z = int(result.group('z'))

            name = orbits.pop(0)
            moons[name] = obj(x, y, z)

    return moons


def unit_tests():
    moons = extract_positions('sample1.txt')
    for i in range(10):
        apply_time_step(moons)
    total = 0
    for m in moons:
        total = total + moons[m].total_energy()
    assert(total == 179)

    moons = extract_positions('sample2.txt')
    for i in range(100):
        apply_time_step(moons)
    total = 0
    for m in moons:
        total = total + moons[m].total_energy()
    assert(total == 1940)


if __name__ == '__main__':

    unit_tests()

    # Production run
    moons = extract_positions()

    print('After 0 steps:')
    for m in moons:
        report_kinematics(moons[m])
    print('')

    for i in range(1000):
        apply_time_step(moons)

    print('After 1000 steps:')
    for m in moons:
        report_kinematics(moons[m])

    total = 0
    for m in moons:
        local = moons[m].total_energy()
        print('{0}: {1}'.format(m, local))
        total = total + local

    print('Total energy = {0}'.format(total))
