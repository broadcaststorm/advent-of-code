# Day 03

## Choice of data structure

Obviously, we have a grid or matrix of data with which we need
to interact. The key to efficiently solving the problem will
hinge on how the input data is stored/accessed.

In C or Fortran (yeah, laugh it up), a two dimensional array
is part of the core language.  In Python, we could replicate a
2D array similarly to C (a list of lists).

In my case, I decided to go the dictionary route whose keys are
(x, y) tuples. By rule, unless it's changed since the dark ages,
keys must be immutable so it has to be a tuple and not a list.

This gives you the advantage of sparsely populating the matrix
if it is freaking huge.

## Building the matrix

I essentially sacrificed computation and memory for a bit of readability.

I read the entire file into memory one line at a time in order to strip
the end of line characters. Then, looped over all the lines again to parse
and build the matrix.

I could have kept track of x and y index values here and built the matrix
out in this single loop as such:

```python
with open(input_file, 'r') as f:
    y = 0
    for line in f.readlines():
        x = 0
        for char in line.rstrip():
            matrix[(x,y)] = char
            x = x + 1
        y = y + 1        

return x, y, matrix
```

At the time, that seemed like it would've been a lot of typing and fraught
with "off by 1" error perils.  In hindsight, that doesn't actually seem bad.
Oh well.

## Repeating the matrix "to the right"

Given the various slopes and the problem description, it was clear we were
going to traverse far past the right of the input data before we got to the
bottom. So the question is, how to handle that?

In a world of infinite memory, you simply clone the structure on demand.
In the world of programming, modulus math keeps you in the bounds and
"wraps around" so that you never run off the edge. 

In my approach for day 03, I figured I didn't need retain the REAL x/y location
(which would have had x >> edge) so I didn't preserve it. However, one could
easily preserve it and simply use the modulus math when accessing the matrix.
