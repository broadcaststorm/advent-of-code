#!/usr/bin/env python3


def parse_image(wide, tall, line):
    """
    parse_image(wide, tall, line):  Given the width and height of a image,
    build a dictionary using tuple x,y as keys and values being lists of
    the layer pixel values.

    d = { (x, y) : [ l1, l2, ... ] }
    """

    pixels = wide * tall

    image = {}

    for i in range(wide):
        for j in range(tall):
            image[(i, j)] = []

    for p in range(len(line)):
        grid = p % pixels
        j = grid // wide
        i = grid % wide

        image[(i, j)].append(line[p])

    return image


if __name__ == '__main__':
    wide = 25
    tall = 6
    layer = wide * tall

    with open('part1.txt', 'r') as f:
        line = f.readline()

    image = parse_image(wide, tall, line)

    # With the image generated, for each layer (z), loop over the w x h
    # grid and simply count the 0, 1, and 2 values.

    counts = []
    max_counts = 1e10
    max_layer = len(line) // layer
    for z in range(max_layer):
        # Add another layer for counts of 0, 1, and 2
        counts.append([0, 0, 0])

        # Loop of this image layer
        for i in range(wide):
            for j in range(tall):
                if image[(i, j)][z] == '0':
                    counts[z][0] = counts[z][0] + 1
                if image[(i, j)][z] == '1':
                    counts[z][1] = counts[z][1] + 1
                if image[(i, j)][z] == '2':
                    counts[z][2] = counts[z][2] + 1

        if counts[z][0] < max_counts:
            max_counts = counts[z][0]
            max_layer = z

    print('WxB value: {0}'.format(counts[max_layer][1] * counts[max_layer][2]))
