#!/usr/bin/env python3


def safety_check(report: list[int]) -> bool:
    """
    A report is safe under the following conditions:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """

    # let's identify increasing or decreasing requirement
    delta = report[-1] - report[0]
    if delta > 0:
        ascending: bool = True
    elif delta < 0:
        ascending: bool = False
    else:
        # Failed condition 2 before we even started!
        return False

    # Now, let's loop through them all
    for i in range(len(report)-1):
        delta = report[i+1] - report[i]

        # Fail condition 1
        if (delta < 0 and ascending) or (delta > 0 and not ascending):
            return False

        # Fail condition 2
        if abs(delta) < 1 or abs(delta) > 3:
            return False

    # We made it through the report so we pass!
    return True


def check_reports(reports: list[list[int]]) -> int:
    safe_reports = 0
    for report in reports:
        if safety_check(report):
            safe_reports += 1
    return safe_reports


def read_input(filename: str) -> list[list[int]]:

    reports: list[list[int]] = list()

    with open(filename, "r") as f:
        for line in f.readlines():
            rept = [ int(x) for x in line.strip().split() ]
            reports.append(rept)

    return reports


def main(filename="../input.txt") -> int:
    report_list = read_input(filename)    
    total_safe = check_reports(report_list)
    return total_safe


if __name__ == '__main__':
    total = main()

    print(f"Answer for part 1: {total}")
