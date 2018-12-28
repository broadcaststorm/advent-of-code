#!/usr/bin/env python3
"""
Recursive fun!

Since each node has a string of recursively embedded nodes within the
node, you can't get the metadata of the "outside" node until you 
recursively process each embedded node... which in turn could have 
embedded nodes on their own.

Must use recursive function to be able to give us a point to the start
of the metadata region after processing the embedded nodes.

"""

def get_metadata(node):
    """
    Return the metadata (second argument) and the element index right 
    after the metadata. 
    """

    # If I've reached a node with no kids, simply return metadata
    nkids, ndata = node[0], node[1]
    if nkids == 0:
        return 2+ndata, node[2:2+ndata]

    # If I have kids, loop over each node in the data and extract
    # the metadata
    mdata = []
    start = 2

    for k in range(nkids):
        elements, kdata = get_metadata(node[start:])
        start = start + elements
        mdata = mdata + kdata

    # Start is where the end of all the child node data ends
    # So now collect the metadata for THIS node
    mdata = mdata + node[start:start+ndata]
    return start+ndata, mdata


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        line = f.readline()
        line.rstrip()

    numbers = []
    for i in line.split():
        numbers.append(int(i))

    elements, metadata = get_metadata(numbers)

    sum = 0
    for i in metadata:
        sum = sum + i

    print('Puzzle 1: {}'.format(sum))
