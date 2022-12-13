#!/usr/bin/env python3
"""
2022/template/solution.py: Python based solution in template folder
"""

from typing import List, Tuple, Set, Dict


def find_most_trees(forest: List[List]) -> Dict:
    """
    find_most_trees(forest) - iterate around the forest and calculate the
    scenic score for all interior trees (not on the perimeter). This time,
    I'll return a dictionary of all scores: key is (row, col) and value is
    the scenic score
    """

    scenic_scores = dict()

    # Get size of forest
    num_rows = len(forest)
    num_cols = len(forest[0])

    # Loop over all inner trees
    for row in range(1, num_rows-1):
        for col in range(1, num_cols-1):
            current_height = forest[row][col]
            current_score = 1

            # Now need to look up and count trees smaller than me
            for i, srow in enumerate(range(row-1, -1, -1)):
                if forest[srow][col] < current_height:
                    continue
                break
            current_score *= i+1

            # Now need to look down
            for i, srow in enumerate(range(row+1, num_rows)):
                if forest[srow][col] < current_height:
                    continue
                break
            current_score *= i+1

            # Now look right
            for i, scol in enumerate(range(col+1, num_cols)):
                if forest[row][scol] < current_height:
                    continue
                break
            current_score *= i+1

            # Now look left
            for i, scol in enumerate(range(col-1, -1, -1)):
                if forest[row][scol] < current_height:
                    continue
                break
            current_score *= i+1

            scenic_scores[(row,col)] = current_score

    return scenic_scores


def find_tall_trees(forest: List[List]) -> Set[Tuple]:
    """
    find_tall_trees(forest) - go around the forest and iterate in straight
    lines to find the tallest, visible trees.  For example, all outer edge
    trees are seen.  Then find trees at least one taller than the one before
    it.
    """

    # Get size of forest
    num_rows = len(forest)
    num_cols = len(forest[0])

    # Returning values
    tall_trees = set()

    # Vertical lines of sight
    for col in range(num_cols):

        previous_tall_down = -1
        previous_tall_up = -1

        for row in range(num_rows):
            # Top Down View
            if forest[row][col] > previous_tall_down:
                previous_tall_down = forest[row][col]
                tall_trees.add((row, col))
            # Bottoms Up View
            b_row = num_rows-row-1
            b_col = num_cols-col-1
            if forest[b_row][b_col] > previous_tall_up:
                previous_tall_up = forest[b_row][b_col]
                tall_trees.add((b_row, b_col))

    # Horizontal lines of sight
    for row in range(num_rows):

        previous_tall_right = -1
        previous_tall_left = -1

        for col in range(num_cols):
            # Left side, looking right
            if forest[row][col] > previous_tall_right:
                previous_tall_right = forest[row][col]
                tall_trees.add((row, col))
            # Right side, looking left
            r_row = num_rows-row-1
            r_col = num_cols-col-1
            if forest[r_row][r_col] > previous_tall_left:
                previous_tall_left = forest[r_row][r_col]
                tall_trees.add((r_row, r_col))

    return tall_trees


def load_forest(filename: str) -> List[List]:
    """
    load_forest(filename) - give the filename, load into a list of lists the
    contents/size of each tree (value).

    The first index is row, the second index is col.  Count starts in upper
    right as 0,0 with row increasing down, and col increasing to right
    """

    forest = list()
    with open(file=filename, mode='r', encoding='UTF-8') as f_obj:
        for line in f_obj:
            forest.append(
                [
                    int(x) for x in list(line.strip())
                ]
            )

    return forest


def part1(filename: str = 'input.txt'):
    """
    part1(filename) - solve Day 8, Part 1
    """

    forest = load_forest(filename)

    tall_trees = find_tall_trees(forest)

    return len(tall_trees)


def part2(filename: str = 'input.txt'):
    """
    part2(filename) - solve Day 8, Part 2
    """

    forest = load_forest(filename)

    scenic_scores = find_most_trees(forest)

    scores = sorted(scenic_scores.values())
    return scores[-1]


if __name__ == '__main__':

    # Solve part1
    result = part1(filename='input-part1.txt')
    print(f'Result is {result}')

    # Solve part2
    output = part2(filename='input-part1.txt')
    print(f'Output is {output}')
