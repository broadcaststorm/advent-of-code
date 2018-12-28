#!/usr/bin/env python3
"""
Same recursive philosophy, different method of calculation to solve
the problem.
"""


def get_metadata(node):
    """
    Return the metadata (second argument) and the element index right
    after the metadata.
    """

    # If I've reached a node with no kids, simply return metadata
    nkids, ndata = node[0], node[1]
    if nkids == 0:
        sum = 0
        for i in node[2:2+ndata]:
            sum = sum + i
        return 2+ndata, sum

    # If I have kids, loop over each node in the data and extract
    # the metadata
    start = 2
    child = [0]*nkids

    for k in range(nkids):
        elements, sum = get_metadata(node[start:])
        child[k] = sum
        start = start + elements

    # Start is where the end of all the child node data ends and this
    # nodes metadata starts.  Loop over those entries get node value
    sum = 0
    for i in node[start:start+ndata]:
        if i > nkids or i < 1:
            continue
        sum = sum + child[i-1]

    return start+ndata, sum


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        line = f.readline()
        line.rstrip()

    numbers = []
    for i in line.split():
        numbers.append(int(i))

    elements, sum = get_metadata(numbers)

    print('Puzzle 2: {}'.format(sum))
