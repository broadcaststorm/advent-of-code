#!/usr/bin/env python3
"""
2022/template/solution.py: Python based solution of Day 7 - No Space Left on Device

Step one is to parse through the file to build a directory structure.
Step two is to build a recursive directory size routine
"""

from typing import List
import copy


class DirTree(object):
    """
    DirTree(object) - a class to represent a file system tree that has the
    properties of current working directory (current_path), space consumption
    tracking for current and subdirectory files, etc.
    """

    def __init__(self):
        self.data = dict()
        self.size = { "/": 0 }
        self.top()

    def top(self):
        """
        top() - reset current path to the root
        """
        self.current_path = list()

    def down(self, subdir: str):
        """
        down(subdir) - descend into the subdir directory
        """
        self.current_path.append(subdir)

    def up(self):
        """
        up() - ascend up one level in the directory tree
        """
        self.current_path.pop()

    def insert(self, new_key, new_value):
        """
        insert(entry, value) - in the current path, insert the new entry
        using new_key as the reference and initialize it to value new_value

        Note: new_value will be a {} for directories and an int file size
        for files.
        """

        # Start at the top
        root = self.data

        # Descend the path
        for p in self.current_path:
            root = root[p]

        root[new_key] = new_value

    def list(self):
        """
        list() - list all entries in the current path
        """

        # Start at the top
        root = self.data

        # Descend the path
        for p in self.current_path:
            root = root[p]

        return list(root.keys())

    def init_size(self, dir_name):
        """
        init_size(dir_name) - on new directory creation, set initial size
        to zero.
        """

        new_path = self.current_path + [dir_name]
        new_key = '/' + '/'.join(new_path)
        self.size[new_key] = 0

    def add_size(self, new_size):
        """
        add_size(new_size) - when a file is stored in the directory, record
        its space consumption in the current path, and all superior directory
        entries.
        """

        this_path = copy.deepcopy(self.current_path)
        while len(this_path) > 0:
            current_key = '/' + '/'.join(this_path)
            self.size[current_key] += new_size
            this_path.pop()

        # Don't forget '/'!
        self.size['/'] += new_size

    def get_size(self, requested_path=None) -> int:
        """
        get_size(requested_path) - if provided, return the disk space usage
        for that directory (and all subdirectories).  If not provided, the
        current path is used.
        """

        if requested_path is None:
            requested_path = '/' + '/'.join(self.current_path)

        if requested_path not in self.size:
            raise Exception(f'Path {requested_path} not found.')

        return self.size[requested_path]

    def create_dir(self, dir_name: str):
        """
        create_dir(dir_name) - add a directory entry to the current
        path with the name dir_name. Initialize the directory size to 0
        """

        self.insert(dir_name, dict())
        self.init_size(dir_name)

    def add_file(self, file_name: str, file_size: int):
        """
        add_file(file_name, file_size) - add a file entry to the current
        path with the name file_name. Store separate the file_size.
        """

        self.insert(file_name, file_size)
        self.add_size(file_size)


def process_input_file(filename: str):
    """
    process_input_file(filename) - using the input file, reconstruct the
    directory structure as a Python dict.

    - I need to have a state element to this (currently listing files)
    - A way to track my current path in the tree
    - A means to store data at the current depth in the tree
    """

    directory_tree = DirTree()

    with open(file=filename, mode='r', encoding='UTF-8') as f_opt:
        for line in f_opt:
            # Let's split the line into "words"
            words = line.strip().split()

            # Is this a command?
            if words[0] == "$":

                # File listing is now over.
                listing_files= False

                # Change directory
                if words[1] == 'cd':
                    if words[2] == '/':
                        directory_tree.top()
                        continue
                    if words[2] == '..':
                        directory_tree.up()
                        continue
                    directory_tree.down(words[2])
                    continue

                # List files
                if words[1] == 'ls':
                    listing_files = True
                    continue

            # Error checking
            if not listing_files:
                raise Exception("Not a command but not listing files")

            # Listing files, is this a directory entry?
            if words[0] == "dir":
                # Store the directory entry
                directory_tree.create_dir(words[1])
                continue

            # Listing files, must be a number
            directory_tree.add_file(words[1], int(words[0]))

    return directory_tree


def get_sizes(pstree: DirTree, path_size: int) -> List[int]:
    """
    get_sizes(pstree, path_size) - return a list of directory sizes for
    paths that have a total size (including subdirectory count) less than
    the path_size provided.
    """

    return [
        size for path, size in pstree.size.items() if size <= path_size
    ]


def part1(filename: str = 'input.txt'):
    """
    part1(filename) - Open the file, read in and reconstruct the directory
    structure. Then walk the tree to find sizing information.
    """

    # Homage to the Linux util :)
    pstree = process_input_file(filename=filename)

    # Get all the size entries less than 100k
    sub_100k = get_sizes(pstree, 100000)

    return sum(sub_100k)


def part2(filename: str = 'input.txt'):
    """
    part2(filename) - Open the file, read in and reconstruct the directory
    structure. Then walk the tree to find sizing information.
    """


    # Homage to the Linux util :)
    pstree = process_input_file(filename=filename)

    total_device_memory = 70000000
    required_free_space = 30000000
    total_consumed_memory = pstree.get_size('/')

    current_unused = total_device_memory - total_consumed_memory
    min_space_to_delete = required_free_space - current_unused

    # Instead of get_sizes which returns results up to a given max, I need
    # to get results that have a given minimum

    potential_sizes = [
        size
        for path, size in pstree.size.items()
        if size >= min_space_to_delete
    ]

    potential_sizes.sort()
    return potential_sizes[0]


if __name__ == '__main__':

    # Solve part1
    result = part1(filename='input-part1.txt')
    print(f'Result is {result}')

    # Solve part2
    output = part2(filename='input-part1.txt')
    print(f'Output is {output}')
