#!/usr/bin/env python3

def is_safe(report):
    """
    Check if a report is safe.
    
    A report is considered safe if:
    1. Its levels are either all increasing or all decreasing.
    2. Each level differs by at most 3 from its previous level.
    3. Each adjacent pair of levels differs by at least 1.

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

def count_safe_reports(input_file):
    """
    Count the number of safe reports.
    
    Parameters:
    input_file (str): The path to the input file containing the reports.
    
    Returns:
    int: The number of safe reports.
    """
    with open(input_file, 'r') as f:
        reports = [line.strip().split() for line in f.readlines()]
    return sum(1 for report in reports if is_safe([int(level) for level in report]))

def main():
    input_file = 'input.txt'
    safe_reports_count = count_safe_reports(input_file)
    print(f'The number of safe reports is {safe_reports_count}')

if __name__ == '__main__':
    main()
