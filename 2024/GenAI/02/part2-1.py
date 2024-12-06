#!/usr/bin/env python3

def is_safe(report):
    """
    Check if a report is safe.
    
    A report is considered safe if:
    1. Its levels are either all increasing or all decreasing.
    2. Each level differs by at most 3 from its previous level.
    3. Each adjacent pair of levels differs by at least 1.

    If removing one level makes the report safe, it also counts as safe.

    Parameters:
    report (list): A list of numbers representing the levels in a report.
    
    Returns:
    bool: True if the report is safe, False otherwise.
    """
    increasing = all(a <= b for a, b in zip(report[:-1], report[1:]))
    decreasing = all(a >= b for a, b in zip(report[:-1], report[1:]))

    # Check levels are either all increasing or all decreasing
    if not (increasing or decreasing):
        return False

    # Check each level differs by at most 3 from its previous level
    if not all(abs(b - a) <= 3 for a, b in zip(report[:-1], report[1:])):
        return False

    # Check each adjacent pair of levels differs by at least 1
    if not all(abs(b - a) >= 1 for a, b in zip(report[:-1], report[1:])):
        return False

    return True


def is_safe_dampened(report):
    """
    Check if a report is safe with the Problem Dampener.

    A report is considered safe if:
    1. It's originally safe.
    2. Removing one level makes it safe.

    Parameters:
    report (list): A list of numbers representing the levels in a report.
    
    Returns:
    bool: True if the report is safe, False otherwise.
    """
    for i in range(len(report)):
        temp_report = report[:i] + report[i+1:]
        if is_safe(temp_report):
            return True
    return is_safe(report)


def count_safe_reports(input_file):
    """
    Count the number of reports that are now safe with the Problem Dampener.

    Parameters:
    input_file (str): The path to the input file containing the reports.
    
    Returns:
    int: The number of reports that are now safe.
    """
    with open(input_file, 'r') as f:
        reports = [line.strip().split() for line in f.readlines()]
    return sum(1 for report in reports if is_safe_dampened([int(level) for level in report]))


def main():
    input_file = 'input.txt'
    safe_reports_count = count_safe_reports(input_file)
    print(f'The number of reports that are now safe with the Problem Dampener is: {safe_reports_count}')


if __name__ == '__main__':
    main()
