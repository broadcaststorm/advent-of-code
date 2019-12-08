#!/usr/bin/evn python3
"""
part2.py

Since the top most solid pixel is that one that is visible, simply iterate
through the x,y grid and the first solid pixel in the layer list is the
value seen.

I built a data structure to save those values but in the end I simply
create a string on each row iteration and printed it out.
"""

from part1 import parse_image


if __name__ == '__main__':
    wide = 25
    tall = 6
    layer = wide * tall

    with open('part1.txt', 'r') as f:
        line = f.readline()

    image = parse_image(wide, tall, line)

    final_image = {}
    for j in range(tall):
        text = []
        for i in range(wide):
            idx = (i, j)

            for p in image[idx]:
                # Transparent, skip
                if p == '2':
                    continue

                # Solid color (0 = black, 1 = white)
                final_image[idx] = p
                if p == '0':
                    text.append('.')
                else:
                    text.append('X')
                break

        print(''.join(text))
