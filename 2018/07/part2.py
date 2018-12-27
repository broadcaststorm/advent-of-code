#!/usr/bin/env python3
"""
The novel twist is that we can complete this work in parallel so that
as the queue gets work, more than one worker can complete it.

The screwy twist on part 2 is that each amount of work takes a different
amount of time.  So, a real queueing system.

Rather than be fancy about and track who completes when, I simply used
an infinite loop clock and changed the work element that gets queued
to be data structure that includes a completion time.

To simplify the code, I created a data structure that mapped the units
to their numeric value so I could just reference it.
"""

import re
import operator


def regex():
    s = r'Step (?P<before>\w) must be finished'
    s = r'{} before step (?P<after>\w) can begin.'.format(s)
    c = re.compile(s)

    return c


def satisfy_requirements(requirements):
    for r in requirements:
        # No, pre-req not met
        if r not in final:
            return False

    return True


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
    clock = 0

    offsets = {}
    for i in range(65, 91):
        offsets[chr(i)] = i - 64

    # 5 workers
    workers = [('', 0)]*5
    following[''] = []
    base = 60

    # Begin loop over clock seconds
    while(True):
        work_completed = False

        for i in range(0, len(workers)):
            # End of processing, store completed work
            if workers[i][1] == clock:
                final.append(workers[i][0])

                # Add the followers to the work list
                work = list(set(work + following[workers[i][0]]))

                # Mark the worker as idle
                workers[i] = ('', -1)

                # Need to account for worker 3 giving worker 0 work now
                work_completed = True

            # Idle worker, assign work
            if workers[i][0] == '':
                # If no work to assign, skip to next worker
                if len(work) == 0:
                    continue

                # Sort the work
                work.sort()

                # Find the next available work to assign
                for j in range(0, len(work)):
                    w = work[j]

                    # Found one
                    if satisfy_requirements(dependencies[w]):
                        workers[i] = (w, clock + base + offsets[w])

                        # Remove from work queue
                        work.pop(j)
                        break

        # Worker management complete.
        if work_completed:
            # If a worker freed up some work, redo worker scan to see
            # if an idle worker can take some more work
            continue

        # Let's see if we are all done
        if len(work) == 0:
            # Are the workers all done?
            for w in workers:
                # No, continue working
                if w[0] != '':
                    break
            # All the workers are idle, exit clock loop
            else:
                break

        # End of clock tick
        clock = clock + 1

    print('Puzzle 2: {}'.format(clock))
    print(''.join(final))
