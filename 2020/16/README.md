# Day 6 Analyis

In general, there are a lot of set operations in this solution to simplify
"the process of elimination".  The result shown is "as written" but I definitely
in hindsight can see a couple improvements to maintain sets across the solution
and reduce the number of conversions.

The one part of my solution that was a gamble (not knowing part 2) was exploding
out the range of values into full lists of integers.  The purpose of that was
clearly to have a Pythonic way of detecting "item in list" type conditionals
and enable the set math.

That could've blown up in my face for part two if I had to track which half of the
"or" the values fell in.  Whew, I'm glad it didn't!

## Part 1

This part seemed to beg for 'set' math. For a given list of numbers on the ticket,
did any of them **not** exist in ALL the valid ranges.  Before looping through the
tickets, make one large set of all valid numbers and then
set(ticket_nums) - set(all_nums). Boom.

## Part 2

Across all tickets, the given columns map to the exact same fields and the
values across all the tickets will constrain the potential fields.  In short,
a nasty process of elimination.  The question is, how to do it effectively.

Option 1:
  - Create a list with the same size as the number of fields
  - Each element of the list is a complete list of the potential fields (valid_ranges.keys())
  - For each ticket
    - For each position
      - Loop over remaining fields in the list
      - if tkt[pos] not in valid[field] (range of values), pop field from list

Option 2:
 - Pull all i-th elements of each ticket into a set()
 - Loop over each valid range to identify which field's set() are completely valid.
 - That identifies the list of fields 

I felt like option two was probably the cleanest code to write, even if I didn't an
elegant loop format ("crude" for i in range(x) approach).

The result, unfortunately, was that the positions did not cleanly result in a single
field candidate for each position as we saw in the second sample example they provided.
So we have to have a second round of logical deduction similarly to Sudoku.

So, based on the example, I need a way to quickly sort the positions from smallest number
of fields to largest while still maintaining their original position number.

Augmenting Option 2 above, when I append to the field_names, I'm going to actually append
a tuple:
   ( len(candidates), candidates, position )

Now I can sort the field_names (which by default sorts on the first element of the tuple)
and start the process of elimination.
