#!/usr/bin/env python3


def valid_node(node, size):
    # Fell off the beginning edges of the grid
    if (node[0] < 0) or (node[1] < 0):
        return False

    # Fell off the end edges of the grid
    if (node[0] >= size[0]) or (node[1] >= size[1]):
        return False

    return True


def calculate_antinodes(locations: list[tuple], grid_size: tuple[int, int]) -> list[tuple]:
    antinodes = list()

    for i, node_a in enumerate(locations):
        for j, node_b in enumerate(locations[i+1:]):
            dx, dy = (node_b[0] - node_a[0], node_b[1] - node_a[1])

            b_node = (node_b[0] + dx, node_b[1] + dy)
            if valid_node(b_node, grid_size):
                antinodes.append(b_node)

            a_node = (node_a[0] - dx, node_a[1] - dy)
            if valid_node(a_node, grid_size):
                antinodes.append(a_node)

    return antinodes


def find_antinodes(antennas: dict, grid_size: tuple[int, int]) -> dict:
    antinodes = dict()

    # First, find all the unique frequencies
    frequencies = set(antennas.values())

    # Select locations for a given frequency
    for freq in frequencies:
        locations = [
            loc for loc, f in antennas.items() if f == freq
        ]

        freq_antinodes = calculate_antinodes(locations, grid_size)
        for loc in freq_antinodes:
            antinodes[loc] = "#"

    return antinodes


def read_input(filename) -> dict:
    antennas = dict()

    with open(filename, "r") as f:
        for row, line in enumerate(f.readlines()):
            for col, char in enumerate(line.strip()):
                if char != '.':
                    antennas[(row, col)] = char

        grid_size = (row+1, col+1)

    return antennas, grid_size


def count_antinodes(antinodes) -> int:
    return len(antinodes.keys())


def print_antinodes(antinodes, size):
    output = list()

    for row in range(size[0]):
        output.append(['.']*size[1])

    for loc, v in antinodes.items():
        output[loc[0]][loc[1]] = v

    print(size)
    for row in output:
        print(row)


def main(filename: str = "puzzle-input.txt") -> int:
    antennas, grid_size = read_input(filename)
    antinodes = find_antinodes(antennas, grid_size)
    # print_antinodes(antinodes, grid_size)
    num_anti_nodes = count_antinodes(antinodes)
    return num_anti_nodes


if __name__ == '__main__':
    total: int = main()

    print(f"Answer for part 1: {total}")
