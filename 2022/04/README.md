# Day 5, Year 2022

Another problem that involves finding overlaps in sets.  In today's solution though, we leverage the superset and subset functionality.  To be able to get to sets, however, we have to parse the ranges string and generate full lists (for generic use cases) which then are collapsed to sets for our specific operations.

## Commentary

After both parts are complete, we certainly could have left the range() output as the iterator and forced instantiation of the range when the conversion to set() was required. That approach would definitely save space as only one complete copy per elf would be needed in memory at that point.
