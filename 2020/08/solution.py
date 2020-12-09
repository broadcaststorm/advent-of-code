#!/usr/bin/env python3


class CPU:
    def __init__(self, commands, accumulator=0):
        # Part 2 - moved contents of init to reset method
        self.reset(commands, accumulator)

    def valid_index(self):
        if self.current < 0 or self.current >= self.__max_inst__:
            return False
        return True

    def is_duplicate(self):
        if self.current in self.executed:
            return True

        return False

    # Part 2 Addition
    def end_of_commands(self):
        if self.current == self.__max_inst__:
            return True
        else:
            return False

    # Part 2 Addition
    def reset(self, commands, accumulator=0):
        self.accumulator = accumulator
        self.instructions = commands
        self.current = 0
        self.executed = []
        self.__max_inst__ = len(self.instructions)

    def process(self):
        """
        Begin processing all stored instructions from wherever the current
        index point is indicating. Exit when a duplicate instruction occurs
        """
        while(not self.is_duplicate()):
            # Part 2 Addition
            if self.end_of_commands():
                return True

            # Sanity check
            if not self.valid_index():
                raise Exception("Out of Bounds Error")

            self.executed.append(self.current)

            op, val = self.instructions[self.current]
            if op == 'nop':
                self.current = self.current + 1
                continue

            if op == 'jmp':
                self.current = self.current + val
                continue

            if op == 'acc':
                self.accumulator = self.accumulator + val
                self.current = self.current + 1
                continue

            raise Exception("Unknown Op {0}".format(op))

        return


def read_input_data(input_file):

    instructions = []

    with open(input_file, 'r') as f:
        for line in f.readlines():
            op, offset = line.rstrip().split(' ')
            instructions.append((op, int(offset)))

    return instructions


def troubleshoot(previous, commands):
    """
    Part 2 Addition

    Previous is the part1 iteration with the infinite loop condition.
    In its current state, the 'executed' list is all the indexes of the
    operations that were executed before the loop began.

    Commands are the original instruction set from which to generate
    testing CPUs.
    """

    flip = {
        "nop": "jmp",
        "jmp": "nop"
    }

    # First, let's identify the candidate indices (nop/jmp) from the
    # infinite loop set of instructions

    candidates = [
        x for x in previous.executed if previous.instructions[x][0] != 'acc'
    ]

    production = CPU(commands)

    for c in candidates:
        # I probably could've deepcopy here and just replaced the one index
        new_command = (flip[commands[c][0]], commands[c][1])
        test_commands = commands[0:c] + [new_command] + commands[c+1:]
        production.reset(test_commands)

        # If this returns true, we reached the end of the instruction list
        if production.process():
            return production

        # If I get here (next iteration of loop), process() returned 'None'
        # Meaning it had an infinite loop.  Try again!

    # If we make it through all candidates and didn't find anything
    # Call that an error for now.
    raise Exception('Exhausted all candidates with no luck')


if __name__ == '__main__':

    print('Part 1')
    sample_commands = read_input_data('sample.txt')
    sample = CPU(sample_commands)
    sample.process()
    print('Sample: {0}'.format(sample.accumulator))

    commands = read_input_data('input.txt')
    production = CPU(commands)
    production.process()
    print('Result: {0}'.format(production.accumulator))

    print('Part 2')
    previous = production
    final = troubleshoot(previous, commands)
    print('Result: {0}'.format(final.accumulator))
