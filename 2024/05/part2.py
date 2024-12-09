#!/usr/bin/env python3


def calculate_test_patterns(pages):
    test_patterns = set()
    for j, this_page in enumerate(pages):
        for that_page in pages[-1:j:-1]:
            test_patterns.add(f"{that_page}|{this_page}")
    return test_patterns


def read_input(filename: str) -> tuple[set[str], list[tuple]]:

    with open(filename, "r") as f:
        rules, print_jobs = f.read().split('\n\n')

    rules_set = set(rules.split('\n'))
    jobs_data = list()

    for i, job in enumerate(print_jobs.split('\n')):
        pages = job.split(',')
        test_patterns = calculate_test_patterns(pages)
        jobs_data.append((pages,test_patterns))

    return rules_set, jobs_data


def invalid_print_jobs(rules, test_patterns):
    return rules & test_patterns


def repair_job_order(pages, failed_patterns):
    # Recursively go through and repair the order
    changes = False

    for pair in failed_patterns:

        # This rule failed because after was earlier than before
        before, after = pair.split('|')
        b_idx = pages.index(before)
        a_idx = pages.index(after)

        # Check to see if we fixed this on previous iteration
        if b_idx < a_idx:
            continue

        # So take after out of the list (earlier) which shifts remaining list left
        value = pages.pop(a_idx)

        # Insert it after before (which is not the actual b_idx shift everything shifted)
        pages.insert(b_idx, value)

        # Flag another go around
        changes = True

    # If I made changes, I could have broken a rule while changing so check again
    if changes:
        return repair_job_order(pages, failed_patterns)

    return pages


def sum_fixed_jobs(rules, print_jobs) -> int:
    middle_sum: int = 0

    for pages, test_patterns in print_jobs:
        failed_patterns = invalid_print_jobs(rules, test_patterns)
        if not failed_patterns:
            continue

        broken = True
        while(broken):
            pages = repair_job_order(pages, failed_patterns)

            # Okay, after fixing all the ones from before, I could've broken others.
            test_patterns = calculate_test_patterns(pages)
            failed_patterns = invalid_print_jobs(rules, test_patterns)

            if not failed_patterns:
                broken = False

        print(pages)
        middle_sum += int(pages[len(pages)//2])
        
    return middle_sum


def main(filename="sample1.txt") -> int:
    rules, print_jobs = read_input(filename)
    total_sum = sum_fixed_jobs(rules, print_jobs)
    return total_sum


if __name__ == '__main__':
    total = main()

    print(f"Answer for part 2: {total}")
