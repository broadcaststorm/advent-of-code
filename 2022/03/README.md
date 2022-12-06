# Day 3, Year 2022 Challenge

The fundamental task in this challenge was efficiently finding the unique item (a single character) among two halves of a string, and then common to groups of three strings.

A brute force method would involve looping over each group of characters that had be identified (the two halves of a string in part 1, the three consecutive strings in part 2) and simply looking for the common example.

A more elegant approach (at least in Python) is to use the [set](https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset) data type. The description (from the website) says it all:

```
A set object is an unordered collection of distinct hashable objects. Common uses include
membership testing, removing duplicates from a sequence, and computing mathematical
operations such as intersection, union, difference, and symmetric difference.
```

The key aspect of that description of importance to using sets in this problem are the operations, namely the intersection.

## Commentary

Even though I use a common approach (set operations), the way I constructed part1 didn't allow for much re-use of code.  The least elegant part for me was the intersection of the 3 contents where 3 is hardcoded.  A more generic approach would be to use **&=** to allow iteration over a generic number of lines.

