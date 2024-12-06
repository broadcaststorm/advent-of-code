# def calculate_distance(left, right):
#     distances = []
#     sorted_left = sorted(left)
#     sorted_right = sorted(right)

#     i = j = 0
#     while i < len(sorted_left) and j < len(sorted_right):
#         if sorted_left[i] < sorted_right[j]:
#             distances.append(j - i)
#             j += 1
#         else:
#             distances.append(i - j)
#             i += 1

#     # Add distance for unmatched elements
#     remaining = max(0, len(sorted_left) - i)
#     distances.extend([remaining] * (len(sorted_right) - j))

#     return sum(distances)

# def main():
#     with open('input.txt', 'r') as file:
#         lines = [line.strip() for line in file.readlines()]

#     # Split the input into two lists
#     left, right = zip(*[line.split()[0] for line in lines])

#     # Convert lists to integers and calculate distance
#     distance = calculate_distance(left, right)

#     print(f'The total distance between the two lists is {distance}')

# if __name__ == '__main__':
#     main()


# def calculate_distance(left, right):
#     distances = []
#     sorted_left = sorted(map(int, left))
#     sorted_right = sorted(map(int, right))

#     i = j = 0
#     while i < len(sorted_left) and j < len(sorted_right):
#         if sorted_left[i] < sorted_right[j]:
#             distances.append(j - i)
#             j += 1
#         else:
#             distances.append(i - j)
#             i += 1

#     # Add distance for unmatched elements
#     remaining = max(0, len(sorted_left) - i)
#     distances.extend([remaining] * (len(sorted_right) - j))

#     return sum(distances)

# def main():
#     with open('input.txt', 'r') as file:
#         lines = [line.strip() for line in file.readlines()]

#     # Split the input into two lists
#     left_list = [int(num) for num in lines[::2]]
#     right_list = [int(num) for num in lines[1::2]]

#     # Calculate distance
#     distance = calculate_distance(left_list, right_list)

#     print(f'The total distance between the two lists is {distance}')

# if __name__ == '__main__':
#     main()

####  Formal prompt 1 (no example input)
# def find_total_distance(filename):
#     # Read the input file
#     with open(filename, 'r') as f:
#         left_list = [int(x) for x in f.read().strip().split('\n')]
#         right_list = [int(x) for x in f.read().strip().split('\n')]

#     # Sort both lists in ascending order
#     left_list.sort()
#     right_list.sort()

#     total_distance = 0

#     # Pair up the smallest numbers from each list and calculate their differences
#     i = j = 0
#     while i < len(left_list) and j < len(right_list):
#         if left_list[i] < right_list[j]:
#             total_distance += right_list[j] - left_list[i]
#             j += 1
#         else:
#             total_distance += left_list[i] - right_list[j]
#             i += 1

#     # Add the remaining numbers in both lists to the total distance
#     while i < len(left_list):
#         total_distance += left_list[i]
#         i += 1
#     while j < len(right_list):
#         total_distance += right_list[j]
#         j += 1

#     return total_distance

# # Run the function and print the result
# filename = 'input.txt'
# total_distance = find_total_distance(filename)
# print(total_distance)

### Formal prompt 2, example input provided:
def calculate_distance(input_file):
    # Read input from file
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    
    # Split each line into two numbers and store them in a list of pairs
    pairs = [(int(x), int(y)) for x, y in (line.split() for line in lines)]
    
    # Sort each pair according to the first number in the pair
    sorted_pairs = [sorted(pair) for pair in pairs]
    
    # Calculate the total distance between the two lists
    total_distance = sum(abs(x - y) for x, y in zip(sorted_pairs[::2], sorted_pairs[1::2]))
    
    return total_distance

# Test the function with the given input file
input_file = 'input.txt'
answer = calculate_distance(input_file)
print(f"The final answer is {answer}.")
