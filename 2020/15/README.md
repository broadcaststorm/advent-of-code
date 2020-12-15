# Commentary on Day 15

The problem solving approach for this day was very straightforward.
You are given a list of numbers and there is a basic set of rules
that govern how to generate the series of numbers you need in order
to reach a particular iteration.

The rules simply involved looking for the repetition of the most recent
number and, if it occurred, the difference in iteration count became the
new number.

## Part 1

To me, a simple Python list is a natural data structure to use for this.
However, finding the two most recent elements of a given value is tough
with the index() method, which finds index number for a given specified
value but starts at "the left" (index 0) and increases until the value
is found (you can adjust the starting and ending index values).

I had thought there was a "right index" method but my Google search late
at night and haste (started this one right after the challenge was released)
couldn't find it. [I, of course, found it this morning when writing this.]
So, to account for this perceived issue, I treated the list as a stack
(last in, first out) as opposed to a queue (first in, first out) by
prepending the new elements.

## Part 2 - The Data Structure Strikes Back

Each year, there's at least one challenge that isn't easily solvable
with "brute force" because of the scale (30M iterations) - or, more
accurately, the simple, as written approach that would seem logical
(as laid out above). Pushing to the stack and then conducting all
those O(N) searches for values definitely adds up - and progressively
gets slower.

My approach to part 2 flips the data model a bit to use a dictionary
of lists where the key is the "value of interest" (that would have been
pushed onto the stack) and the value is a list of iteration indexes
where that "value of interest" was seen. This approach improved the
computational complexity in two ways:

- Finding the "value of interest" (the number that was spoken) is a
simple hash lookup, rather than iterating through the list.
- Finding the two previous indices is simply grabbing the last two values
on the list of indices. I reverted to 'appended' as I no longer needed
to be concerned with index() vs rindex().

Example of the dictionary (random numbers not from puzzle):

```python
{
    0: [0, 4, 21],
    2: [1, 3, 20],
}
```
