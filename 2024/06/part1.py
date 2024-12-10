#!/usr/bin/env python3


import copy


# Character representing guard and direction facing as the keys,
# the values are the x,y displacement for that direction.
directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

# Don't be fancy, simple map for right turns
right_turn_clyde = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}


def walk_the_lab(lab_map: dict, start: tuple, size: tuple) -> dict:
    guard_path = dict()

    in_lab = True
    current_spot = start

    while(in_lab):
        # Mark current spot
        guard_path[current_spot] = "X"

        # Guard direction
        guard_spot = lab_map[current_spot]
        guard_direction = directions[guard_spot]

        # What's my next spot look like?
        next_spot = (current_spot[0] + guard_direction[0], 
                     current_spot[1] + guard_direction[1])

        # Is it still in the lab?  If not, terminate loop
        if (next_spot[0] < 0) or (next_spot[1] < 0) or (next_spot[0] >= size[0]) or (next_spot[1] >= size[1]):
            in_lab = False
            continue

        # Is it obstructed? If so, change direction and repeat the loop
        if lab_map[next_spot] == "#":
            lab_map[current_spot] = right_turn_clyde[guard_spot]
            continue

        # Path all clear?  Let's go!
        lab_map[next_spot] = lab_map[current_spot]
        current_spot = next_spot

    return guard_path


def read_input(filename: str) -> tuple[dict, tuple, tuple]:
    grid = dict()
    start = tuple()
    size = tuple()

    with open(filename, "r") as f:
        for x, row in enumerate(f.readlines()):
            for y, col in enumerate(row.strip()):
                grid[(x,y)] = col
                if col in directions.keys():
                    start = (x, y)

        size = (x+1, y+1)

    return grid, start, size


def main(filename: str ="puzzle-input.txt") -> int:
    lab_map, guard_start, lab_size = read_input(filename)
    guard_spots = walk_the_lab(lab_map, guard_start, lab_size)
    return len(guard_spots.keys())


if __name__ == '__main__':
    total: int = main()

    print(f"Answer for part 1: {total}")
