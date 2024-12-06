#!/usr/bin/env python3

import numpy as np

def bad_level(report, low, high, ascending):
    """
    We have to identify which value is the one to discard.
    """

    ### This really should happend
    if low == 0:
        bot = low
    else:
        bot = low - 1

    ### I'm at the end of the reports, this means the last value went
    ### counter to the trend (asc/desc) so toss last value
    if high == len(report)-1:
        return high
    else:
        top = high+1

    delta_above = report[high+1] - report[low]
    delta_below = report[high] - report[bot]

    # We have too big a jump but in the correct direction (asc or desc)
    if ascending == None:
        if abs(delta_above) <= 3:
            return high
        if abs(delta_below) <= 3:
            return low

        # Default to removing the next item in list
        print('ping')
        return high

    if ascending:
        # The report beyond the dip is higher, let's go!
        if delta_above > 0:
            return high
        return low
    else:
        if delta_above < 0:
            return high
        return low


def valid_pair(report: list[int], low: int, high: int, ascending: bool) -> bool:
    delta = report[high] - report[low]

    # Fail condition 1
    if (delta < 0 and ascending) or (delta > 0 and not ascending):
        return False

    # Fail condition 2
    if abs(delta) == 0 or abs(delta) > 3:
        return False

    return True


def bad_report(report: list[int], index: int, ascending: bool) -> int:
    """
    Given a list of reports that has failed the safety check,
    identify the bad report to remove and return that index.

    The index given is the lower index of the report and the next
    element in the report list caused the failure.
    """

    # Save on the math, what is the last element number
    last = len(report) - 1
    penult = last - 1

    # Shouldn't happen, but failsafe
    if index == last:
        print("Index too large {index}", report)
        return index

    # The delta that failed
    delta = report[index+1] - report[index]
    rising = True if delta > 0 else False

    # If I'm at the start of the array, don't underrun list
    low = 0 if index == 0 else index - 1

    # If I'm at the end of the array, don't overrun list
    high = last if index == last else index + 2

    # Scenario 1, 2, and 3:
    #  1: Incorrect slope (pair drops when supposed to climb)
    #  2: Incorrect slope (pair climbs when supposed to drop)
    #  3: Two consecutive values are the same
    if (ascending and (not rising)) or ((not ascending) and rising) or (delta == 0) or (abs(delta) > 3):
        # If we are at the end of the report, drop the last tail
        if index == penult:
            return last
        
        # If my jump from current to one beyond is valid, drop the dip
        if valid_pair(report, index, high, ascending):
            return index + 1

        # If I'm at the beginning of the list, drop the current entry
        if index == 0:
            return index
        
        # Check to see of the previous report to next report (that made
        # current delta bad). If so, drop current entry
        if valid_pair(report, low, index+1, ascending):
            return index

        # For now, default to dropping the index causing the failure
        return index + 1

    raise Exception("No bad scenario???")    


def safety_check_dampener(report: list[int], ascending) -> bool:
    """
    A report is safe under the following conditions:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """

    # Now, let's loop through them all
    for i in range(len(report)-1):
        if not valid_pair(report, i, i+1, ascending):
            raise Exception(i)

    # We made it through the report so we pass!
    return True


def check_reports(reports: list[list[int]], slopes: list[bool]) -> int:
    safe_reports = 0

    for i, report in enumerate(reports):
        idx = None

        # First pass, no dampener
        try:
            if safety_check_dampener(report, slopes[i]):
                safe_reports += 1
                print(f"Safe without dampener: {i}")
        except Exception as e:
            idx = int(e.args[0])
            print(f"\tIteration {i}, {idx}", report)

        # Dampener triggered
        if idx is not None:
            # Need to find the element to remove
            bad = bad_report(report, idx, slopes[i])
            print(f"\tRemoving index {bad}:", report.pop(bad))

            try:
                if safety_check_dampener(report, slopes[i]):
                    safe_reports += 1
                    print(f"Safe with dampener: {i}")
            except Exception as e:
                print(f"Unsafe {i}: " + str(report))

    return safe_reports

def generate_slopes(reports) -> list[bool]:
    slopes = list()
    for rept in reports:
        x = np.array(range(1, len(rept)+1))
        y = np.array(rept)
        slope, intercept = np.polyfit(x,y,1)
        if slope > 0:
            slopes.append(True)
        else:
            slopes.append(False)
    return slopes


def read_input(filename: str) -> list[list[int]]:

    reports: list[list[int]] = list()

    with open(filename, "r") as f:
        for line in f.readlines():
            rept = [ int(x) for x in line.strip().split() ]
            reports.append(rept)

    return reports


def main(filename="../input.txt") -> int:
    report_list = read_input(filename)
    slopes = generate_slopes(report_list)
    total_safe = check_reports(report_list, slopes)
    return total_safe


if __name__ == '__main__':
    total = main()

    print(f"Answer for part 2: {total}")
