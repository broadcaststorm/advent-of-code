#!/usr/bin/env python3


import numpy
from part1 import Orbit, apply_time_step, report_kinematics
from part1 import moon_names, extract_positions


class Universe(Orbit):
    def __init__(self, x, y, z):
        Orbit.__init__(self, x, y, z)

    def position(self):
        return [self.x, self.y, self.z]

    def velocity(self):
        return [self.vx, self.vy, self.vz]


class OrbitalTracker:
    def __init__(self):
        self.history = {'x': set(), 'y': set(), 'z': set()}
        self.repeat_interval = {'x': None, 'y': None, 'z': None}

    def record_vectors(self, moons, step):
        positions = list(moons[m].position() for m in moon_names)
        velocities = list(moons[m].velocity() for m in moon_names)

        x_axis = (
            tuple(p[0] for p in positions),
            tuple(v[0] for v in velocities)
        )

        y_axis = (
            tuple(p[1] for p in positions),
            tuple(v[1] for v in velocities)
        )

        z_axis = (
            tuple(p[2] for p in positions),
            tuple(v[2] for v in velocities)
        )

        for dim, axis in [('x', x_axis), ('y', y_axis), ('z', z_axis)]:
            if self.repeat_interval[dim]:
                continue
            if axis in self.history[dim]:
                self.repeat_interval[dim] = step
                continue
            self.history[dim].add(axis)

        # Did I find them all?
        if all(s for s in self.repeat_interval.values()):
            return True
        return False

    def report_intervals(self):
        return list(self.repeat_interval[step] for step in ['x', 'y', 'z'])


def orbit_status(moons, step):
    print('Step {0}:'.format(step))
    for m in moons:
        report_kinematics(moons[m])
    total = 0
    for m in moons:
        local = moons[m].total_energy()
        total = total + local
    print('Total energy = {0}'.format(total))
    print('')


def find_orbits(moons):
    i = 0
    interval = 1000000

    tracker = OrbitalTracker()
    while(True):
        if tracker.record_vectors(moons, i):
            break

        if i % interval == 0:
            orbit_status(moons, i)

        apply_time_step(moons)
        i = i + 1

    orbit_status(moons, i)
    values = tracker.report_intervals()
    return numpy.lcm.reduce(values)


def unit_tests():
    moons = extract_positions('sample1.txt', Universe)
    steps = find_orbits(moons)
    print(steps)
    assert(steps == 2772)
    print('Pass test 1')

    moons = extract_positions('sample2.txt', Universe)
    steps = find_orbits(moons)
    assert(steps == 4686774924)
    print('Pass test 2')


if __name__ == '__main__':
    unit_tests()

    # Production run
    moons = extract_positions(obj=Universe)
    steps = find_orbits(moons)
    print('Steps are: {0}'.format(steps))
