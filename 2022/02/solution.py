#!/usr/bin/env python3
"""
2022/02/solution.py: Python based solution for Day 2 challenge of Rock,
Paper, Scissors
"""

from typing import List, Tuple
from enum import IntEnum


class Points(IntEnum):
    """
    Points(IntEnum) - enumerated data type for scoring
    """
    X = 1
    Y = 2
    Z = 3


class Score(IntEnum):
    """
    Score(IntEnum) - store the scoring relations for win, lose, or draw
    """
    Win = 6
    Draw = 3
    Lose = 0


# StrEnum is in 3.11
loser = {
    "A": "Z", "B": "X", "C": "Y"
}

draw = {
    "A": "X", "B": "Y", "C": "Z"
}

winner = {
    "A": "Y", "B": "Z", "C": "X"
}


def score_rounds_by_results(rounds: List[Tuple]) -> List[int]:
    """
    """

    results = {"X": loser, "Y": draw, "Z": winner}
    score_enum = {"X": "Lose", "Y": "Draw", "Z": "Win"}

    scores = list()

    for yours, result in rounds:
        mine = results[result][yours]
        scores.append(
            Score[score_enum[result]] + Points[mine]
        )

    return scores

def score_rounds_by_fists(rounds: List[Tuple]) -> List[int]:
    """
    score_rounds(rounds): iterate through each round of rock/paper/scissors and
    determine the winner and the score assigned.
    """

    scores = list()
    for yours, mine in rounds:
        if winner[yours] == mine:
            scores.append(Score.Win + Points[mine])
        elif draw[yours] == mine:
            scores.append(Score.Draw + Points[mine])
        elif loser[yours] == mine:
            scores.append(Score.Lose + Points[mine])
        else:
            raise Exception()

    return scores


def get_rounds(filename: str) -> List[Tuple]:
    """
    get_rounds(filename): open the file, extra the rounds of rock/paper/scissor
    """

    with open(file=filename, mode='r', encoding='UTF-8') as fobj:
        content = fobj.read().strip()

    rounds = list()

    for attempt in content.split('\n'):
        yours, mine = attempt.split(' ')

        rounds.append((yours, mine))

    return rounds


def part1(filename: str):

    rounds = get_rounds(filename)
    scores = score_rounds_by_fists(rounds)

    return sum(scores)


def part2(filename: str):
    rounds = get_rounds(filename)
    scores = score_rounds_by_results(rounds)

    return sum(scores)


if __name__ == '__main__':

    # Solve part1
    result = part1(filename='input-part1.txt')
    print(f'Result is {result}')

    # Solve part2
    output = part2(filename='input-part1.txt')
    print(f'Output is {output}')
