# Commentary on Day 2

The crux of the story in day 2 is parsing a string.  In part 1,
we essentially have to count the occurrences of a specific character.
In part 2, it's a tad easier in that we simply have to extract the
character values at two specific locations for comparison.

## Strategies for part 1

As context, in Python, strings is class within the core library that
represents a series of characters with list like behaviors. What does
that mean?

- I can loop over the characters in the string (for c in str)
- I can get the number of characters in the string (len(str))
- I can identify the character at a specific location (str[i])
- I can splice the string (str[i:j])

Strings also have other tools for parsing/processing them, such as
regular expressions.

### Loop and count

Fairly straight forward - almost "brute force" - means for counting
the number of occurrences of particular character:

```python
i == 0
for c in str:
    if c == 'x':
        i = i + 1
print(i)
```

In my solution, I used a "list comprehension" in order to extract
all the occurrences of the target character into another list and
then simply queried the length of the list.

```python
chars = [c for c in str if c == 'x']
print(len(chars))
```

What the list comprehension above does is:
- Loop over str, each iteration assigned to 'c'
- if c == 'x', then add c to the list
- return the built up list to the variable 'chars'

Another way to write my approach above to understand what it is doing:

```python
chars = []
for c in str:
    if c == 'x':
        chars.append(c)
print(len(chars))
```

### Regular expression

I couldn't remember the correct regular expression method when I
was first solving the problem, hence why it's not in either solution.
However, the regular expression module - **re** - has a matching
method *findall* that returns a list of all matches. It has a lot
of interesting use cases but, for this problem, it functions similarly
to my list comprehension:

```python
import re

chars = re.findall(r'x', str)
print(len(chars))
```

## Strategies for Part 2

Honestly, what strategy do you need? You are given two string positions
and one of the two (but not both) needs to match the character specified.
The hard work was in extracting the min, max, char, and password from
each line in part 2 - and that was done in the solution for part 1.

## Refactored solution

I did take the opportunity to refactor the part 1 and part 2 solutions
to showcase passing python methods as arguments to another method as a
way to use the same validation framework but pass two different policies
for validation.
