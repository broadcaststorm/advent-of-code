#!/usr/bin/env python3

def is_safe(report):
    """
    Check if a report is safe.
    
    A report is considered safe if all levels are either increasing or decreasing,
    and each level differs by at least 1 and at most 3 from its previous level.
    
    Parameters:
    report (list): A list of numbers representing the levels in a report.
    
    Returns:
    bool: True if the report is safe, False otherwise.
    """
    increasing = all(a <= b for a, b in zip(report[:-1], report[1:]))
    decreasing = all(a >= b for a, b in zip(report[:-1], report[1:]))
    return (increasing or decreasing) and all(abs(b - a) <= 3 for a, b in zip(report[:-1], report[1:]))

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