def calculate_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Initialize total distance to 0
    total_distance = 0

    # Iterate through the sorted lists
    for i in range(min(len(left_sorted), len(right_sorted))):
        # Calculate the distance between the current pair of numbers
        distance = abs(left_sorted[i] - right_sorted[i])

        # Add the distance to the total distance
        total_distance += distance

    # Return the total distance
    return total_distance


def main():
    # Read the input file
    with open('input.txt', 'r') as f:
        left_list = [int(line.split()[0]) for line in f.readlines()]
        right_list = [int(line.split()[1]) for line in f.readlines()]

    # Calculate and print the total distance
    total_distance = calculate_distance(left_list, right_list)
    print(total_distance)


if __name__ == "__main__":
    main()


"""
# Day 1: Historian Hysteria

### Problem Description

The problem requires us to find the total distance between two lists of location IDs. The lists are sorted in ascending order, but they 
may not be identical.

### Solution

We can solve this problem by using a sorting algorithm and then iterating through the pairs of numbers and calculating their distances.

```python
def calculate_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Initialize total distance to 0
    total_distance = 0

    # Iterate through the sorted lists
    for i in range(min(len(left_sorted), len(right_sorted))):
        # Calculate the distance between the current pair of numbers
        distance = abs(left_sorted[i] - right_sorted[i])

        # Add the distance to the total distance
        total_distance += distance

    # Return the total distance
    return total_distance


def main():
    # Read the input file
    with open('input.txt', 'r') as f:
        left_list = [int(line.split()[0]) for line in f.readlines()]
        right_list = [int(line.split()[1]) for line in f.readlines()]

    # Calculate and print the total distance
    total_distance = calculate_distance(left_list, right_list)
    print(total_distance)


if __name__ == "__main__":
    main()
```

### Example Use Case

To use this script, simply replace `input.txt` with your own input file. The script will read the file, calculate the total distance 
between the two lists, and print it to the console.

Note: Make sure to run the script in a directory where you have write permissions, as the script writes its output to the console.
"""