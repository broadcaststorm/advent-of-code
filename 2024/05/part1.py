#!/usr/bin/env python3

def read_input(filename: str) -> tuple[set[str], list[tuple]]:

    with open(filename, "r") as f:
        rules, print_jobs = f.read().split('\n\n')

    rules_set = set(rules.split('\n'))
    jobs_data = list()

    for i, job in enumerate(print_jobs.split('\n')):
        pages = job.split(',')

        test_patterns = set()
        for j, this_page in enumerate(pages):
            for that_page in pages[-1:j:-1]:
                test_patterns.add(f"{that_page}|{this_page}")

        jobs_data.append((pages,test_patterns))

    return rules_set, jobs_data


def valid_print_jobs(rules, test_patterns):
    if rules & test_patterns:
        return False
    
    return True


def sum_valid_jobs(rules, print_jobs) -> int:
    middle_sum: int = 0

    for pages, test_patterns in print_jobs:
        if not valid_print_jobs(rules, test_patterns):
            continue

        middle_sum += int(pages[len(pages)//2])
        
    return middle_sum


def main(filename="input.txt") -> int:
    rules, print_jobs = read_input(filename)
    total_sum = sum_valid_jobs(rules, print_jobs)
    return total_sum


if __name__ == '__main__':
    total = main()

    print(f"Answer for part 1: {total}")
