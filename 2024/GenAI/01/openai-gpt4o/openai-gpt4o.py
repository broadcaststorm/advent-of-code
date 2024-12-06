def calculate_total_distance(filename='input.txt'):
    # Initialize lists to store the location IDs
    left_list = []
    right_list = []

    # Read the input file
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into two numbers and append to the respective lists
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

    # Output the result
    print(total_distance)

# Execute the function
calculate_total_distance()

"""
To solve this problem, we need to calculate the total distance between two lists of location IDs. Here's a step-by-step breakdown of how to approach this:

1. **Read the Input**: We need to read the input from a file named `input.txt` that contains pairs of numbers separated by spaces. Each line represents a pair of numbers, one from the left list and one from the right list.

2. **Parse the Input**: Extract the numbers from each line and store them into two separate lists: `left_list` and `right_list`.

3. **Sort the Lists**: Sort both `left_list` and `right_list` to ensure we can pair the smallest numbers together as described in the problem.

4. **Calculate Distances**: For each pair of numbers (one from each list), calculate the absolute difference between them and sum these differences to get the total distance.

5. **Output the Result**: Print the total distance to the console.

Below is the Python script to accomplish these tasks:

```python
def calculate_total_distance(filename='input.txt'):
    # Initialize lists to store the location IDs
    left_list = []
    right_list = []

    # Read the input file
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into two numbers and append to the respective lists
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

    # Output the result
    print(total_distance)

# Execute the function
calculate_total_distance()
```

### Explanation of the Script:
- **Reading Input**: We open the `input.txt` file and read each line. For each line, we split the values, convert them to integers, and append them to their respective lists.
- **Sorting**: Both `left_list` and `right_list` are sorted to facilitate correct pairing.
- **Calculating Distances**: We use a generator expression within the `sum` function to calculate the total distance by iterating over the pairs from both lists.
- **Output**: Finally, the total distance is printed.

This script will read the input file, process the data as described in the problem, and print the correct total distance to the command line.

"""