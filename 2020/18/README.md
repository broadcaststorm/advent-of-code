# Day 18 Commentary

I think what made this solution scalable was decoupling the
reduction of the expression inside the **()** and the searching
for that expression.  By extracting away all the **()** handling,
the method that processed the expression based on a given set of
order of operations could be swapped out easily... as I found out
was required in the second part.

## Parenthesis Matching

In short, the regular expression was the key here:

```python
    paren_regex = r'\((?P<expr>(?:\d+? [\+\*] )+\d+?)\)'
```

Let's break it down:

- The "escaped" outer parentheses (anchors) would find a string contained
within a set of (explicit) parentheses.
- That left the secondmost outer parentheses to function as the
regex group to be "captured" into the attribute 'expr' within
a matching object.

The remaining regex looks like this:

```python
(?:\d+? ]\+\*] )+\d+?
```

Which translates to 1 or more patterns of "num op " (e.g. '5 + ' or '6 * 5 + ')
followed by another number.  "Number" in the regex above - **\d+?** - means
1 or more number characters and the **?** adds the constraint to use as few as
possible for the match. The **?** may not be strictly needed in this case but
I find as a habit the non-greedy approach tends to work more intuitively in my
applications.

As a side note: the **?:** at the beginning of the grouping indicates that
Python's *re* should not capture the value inside the parentheses as a match.
In my case, I need the grouping to repeat the pattern but I don't care about
the values it matches... just the overall string match within the anchor
parentheses.

# Part 1

The reduction is fairly straight forward in part 1. The string is a whitespace
separated list of numbers and operations which can be processed in triplets
from left to right.  Effectively shift the first three elements from the head
of the list.  The second element dictates the math to perform, then splice the
result back to the head of the line.  Rinse and repeat.

# Part 2

The reduction gets a little trickier because you have to do all the **add**
operations first.  But, because I'm sending the sub-expression after the
parenthetical searching has been done, I can simply search for all the
add elements in the list, splice out the triplet centered on that '+' index, do the math, insert to result back into the list.  Rinse and repeat for '+'.

When all that is complete, I re-used most of the code from part 1 (removing
the '+' checks) and finished all the math.
