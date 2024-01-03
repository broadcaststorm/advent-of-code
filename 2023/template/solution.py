#!/usr/bin/env python3
"""
2022/template/solution.py: Python based solution in template folder
"""


import typer


app = typer.Typer()


@app.command()
def part1(filename: str = 'input.txt'):
    # Solve part1
    # print(f'Result is {result}')
    pass


@app.command()
def part2(filename: str = 'input.txt'):
    # Solve part2
    # print(f'Output is {output}')
    pass


if __name__ == '__main__':
    app()
