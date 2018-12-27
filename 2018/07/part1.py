#!/usr/bin/env python3
"""
The challenge primarily focuses on dependency trees.  I don't feel like
Python native data structures provide the optimal building blocks for
solving this.

However, I made it work by creating two trees:
  - one where the values are required to complete before the key can be
    processed (a tree indicating pre-requisites)
  - one where the values are the next item that can be matched when the
    key has been processed (forward mapping)

These two trees are needed in my approach because of the interesting
twist of the puzzle - namely, as units are available to be processed
(namely, all their pre-reqs are completed), the next unit to be
processed is based on an alphabetical list of available units.

As units become available, I add the unit to a work queue and, when it
is time to start a new unit, I sort the list. Then, before you can pull
the item from the queue, all its pre-reqs (not just the one that
finished and added it to the queue) must be met.  Hence, the two trees.

"""

import re
import operator
import sys


def regex():
    s = r'Step (?P<before>\w) must be finished'
    s = r'{} before step (?P<after>\w) can begin.'.format(s)
    c = re.compile(s)

    return c


if __name__ == '__main__':

    parser = regex()

    dependencies = {}
    following = {}

    with open('input.txt', 'r') as f:
        for l in f:
            result = parser.match(l)
            before = result.group('before')
            after = result.group('after')

            # Add the dependencies
            if after not in dependencies:
                dependencies[after] = [before]
            else:
                dependencies[after].append(before)

            # Populate the pre-reqs too
            if before not in dependencies:
                dependencies[before] = []

            # Map the other direction, for each item, what is next
            if before not in following:
                following[before] = [after]
            else:
                following[before].append(after)

            # Populate the followers too
            if after not in following:
                following[after] = []

    # The 'dependencies' tree key with 0 length value is the beginning
    # So, generate a list of tuples with length of pre-reqs and key
    counts = []
    for a in dependencies.keys():
        counts.append((len(dependencies[a]), a))

    # Sort the counts
    counts.sort(key=operator.itemgetter(0))

    # Find the various entry points into the workflow
    work = []
    for c in counts:
        if c[0] == 0:
            work.append(c[1])
        else:
            break

    # Prime the final result
    final = []

    while(len(work)):
        # This list must be alphabetically sorted
        work.sort()

        # Loop through the available work
        for i in range(0, len(work)):
            w = work[i]

            # Are the pre-reqs satisfied for this?
            requirements = dependencies[w]
            for r in requirements:
                # No, pre-req not met
                if r not in final:
                    break
            else:
                # Pre-req met, add to final list
                final.append(w)

                # Remove from work list
                work.pop(i)

                # Add the followers to the work list
                work = list(set(work + following[w]))
                break

        # We looped through all the work and none of them met pre-reqs
        else:
            print('Infinite loop prevention')
            sys.exit(1)

    print('Puzzle 1: {}'.format(''.join(final)))
