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


def walk_the_lab(lab_map: dict, start: tuple, size: tuple, block: tuple) -> tuple[dict, bool]:
    guard_path = dict()

    in_lab = True
    current_spot = start

    # Guard direction
    guard_spot = lab_map[current_spot]
    guard_direction = directions[guard_spot]

    # Insert temporary block
    if lab_map[block] == ".":
        lab_map[block] = "#"
    else:
        raise Exception("lab_map[{block}] was {lab_map[block]}")

    # Max grid size
    max_grid = size[0] * size[1]

    # Loop count
    loop_count = 0

    # Walk the lab (add an infinite loop check)
    while(in_lab):
        # (crude) loop check
        if len(guard_path.keys()) > max_grid:
            break

        loop_count += 1
        if loop_count > max_grid:
            break

        # Mark current spot
        guard_path[current_spot] = "X"

        # What's my next spot look like?
        next_spot = (current_spot[0] + guard_direction[0], 
                     current_spot[1] + guard_direction[1])

        # Is it still in the lab?  If not, terminate loop
        if (next_spot[0] < 0) or (next_spot[1] < 0) or (next_spot[0] >= size[0]) or (next_spot[1] >= size[1]):
            in_lab = False
            continue

        # Is it obstructed? If so, change direction and repeat the loop
        if lab_map[next_spot] == "#":
            guard_spot = right_turn_clyde[guard_spot]
            guard_direction = directions[guard_spot]
            continue

        # Path all clear?  Let's go!
        current_spot = next_spot

    # Reset temporary block
    lab_map[block] = "."

    # If "in_lab" is true and I escaped the while(), I must be looping. if "false", I left the lab
    return guard_path, in_lab


def block_the_lab(lab_map: dict, start: tuple, size: tuple) -> int:
    # First, the list of all clear spots
    open_spots: list[tuple] = [
        k for k, v in lab_map.items() if v == "."
    ]

    valid_spots = 0

    for spot in open_spots:
        guard_path, in_lab = walk_the_lab(lab_map, start, size, spot)

        if in_lab:
            valid_spots += 1

    return valid_spots


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


def main(filename: str ="sample1.txt") -> int:
    lab_map, guard_start, lab_size = read_input(filename)
    guard_spots = block_the_lab(lab_map, guard_start, lab_size)
    return guard_spots


if __name__ == '__main__':
    total = main()

    print(f"Answer for part 2: {total}")
