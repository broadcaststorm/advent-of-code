#!/usr/bin/env python3
"""
2022/05/solution.py: Python based solution for Day 5: Supply Stacks
"""

from typing import List, Tuple, Dict

def parse_stack_content(stack_contents: str) -> Dict:
    """
    parse_stack_content(contents): take the string stack definition and
    convert it to a dictionary of stacks (LIFO queues) whose keys are
    the stack numbers.
    """

    # The contents are a single string. Need to generate a list of lines
    contents = stack_contents.split('\n')

    # The last row of the content is the list of stack numbers
    column_names = contents[-1].split()

    # Now, identify the row index for each column name
    # Assumption: no more than 9 columns (otherwise, doesn't align)
    index_names = [
        contents[-1].index(x) for x in column_names
    ]

    # Build the initial stacks
    stacks = {
        n: list() for n in column_names
    }

    # Now, let's work backwards and build the stack
    for line in contents[-2::-1]:
        for i, n in enumerate(column_names):
            if line[index_names[i]] != ' ':
                stacks[n].append(line[index_names[i]])

    return stacks


def parse_instruction_content(instruction_contents: str) -> List[Tuple]:
    """
    parse_instruction_content(instruction_contents) - parse the string of
    instructions and generate a list of tuples containing (qty, from, to)
    """

    # The contents are a single string. Need to generate a list of lines
    contents = instruction_contents.split('\n')

    # Since format is fixed at "move N from X to Y", use some cool list tricks
    # namely, split the string into words, then splice every other word
    # starting at the 2nd word (index 1)

    tupletizer = lambda x: (int(x[0]), x[1], x[2])
    instructions = [
        tupletizer(line.split()[1::2]) for line in contents
    ]

    return instructions


def extract_stacks_and_instructions(filename: str) -> Tuple[Dict, List]:
    """
    extract_stacks_and_instructions(filename) - open the file by name and
    extract the initial crate stack configuration as well as the list of
    relocation instructions.

    Return two elements (tuple): a dictionary of LIFO queues (stacks),
    each stack referenced by their character stack number. and a list of
    tuples containing three elements: qty, from stack, to stack.
    """

    # Given the file has stacks, blank line, and instructions, let's be lazy:
    with open(file=filename, mode='r', encoding='UTF-8') as f_obj:
        contents = f_obj.read()

    # Splitting by the blank line easily partitions stacks from instructions
    stack_content, instruction_content = contents.split('\n\n')

    # Parse the contents separately
    stacks = parse_stack_content(stack_content)
    instructions = parse_instruction_content(instruction_content)

    return stacks, instructions


def process_stacks(stacks: Dict, instructions: List[Tuple], preserve_order=False) -> Dict:
    """
    process_stacks(stacks, instructions): take the list of tupled instructions
    and restack all the stacks as directed.  Returned the updated stacks.

    preserve_order = False: block is moved one at a time, group of 5 blocks
    order is inverted in destination compared to the source

    preserve_order = True: entire block group is relocated to new stack, order
    is preserved, e.g. blocks 4,5,6 in stack 1 will have an order 1,2,3 in
    new stack 10.
    """

    for quantity, from_stack, to_stack in instructions:
        if not preserve_order:
            while quantity > 0:
                stacks[to_stack].append(
                    stacks[from_stack].pop()
                )
                quantity -= 1
        else:
            stacks[to_stack].extend(
                stacks[from_stack][-quantity:]
            )
            del stacks[from_stack][-quantity:]

    return stacks


def pop_top_entries(stacks: Dict) -> List[str]:
    """
    pop_top_entries(stacks) - go through each stack in order and return
    the ordered list of top/last entries in each stack. I could have relied
    on recent Python default behavior to preserve dictionary key order.
    Instead, I'll rely on the fact that the column keys are simply numbers.
    """

    return [
        stacks[str(n+1)][-1] for n in range(len(stacks))
    ]


def part1(filename: str = 'input.txt'):
    """
    part1(filename) - solve the Day 5, Year 2022 part 1 challenge
    """

    stacks, instructions = extract_stacks_and_instructions(filename)

    restacked = process_stacks(stacks, instructions)
    top_entries = pop_top_entries(restacked)

    return "".join(top_entries)


def part2(filename: str = 'input.txt'):
    """
    part1(filename) - solve the Day 5, Year 2022 part 1 challenge
    """

    stacks, instructions = extract_stacks_and_instructions(filename)

    restacked = process_stacks(stacks, instructions, preserve_order=True)
    top_entries = pop_top_entries(restacked)

    return "".join(top_entries)


if __name__ == '__main__':

    # Solve part1
    result = part1(filename='input-part1.txt')
    print(f'Result is {result}')

    # Solve part2
    output = part2(filename='input-part1.txt')
    print(f'Output is {output}')
