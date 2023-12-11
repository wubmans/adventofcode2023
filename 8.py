from math import floor
from functools import cmp_to_key
import re


def parse_input(filename):

    directions = None

    nodes = {}
    
    file = iter(open(filename).readlines())
    for line in file:
        line = re.sub(r'\n', '', line)
        if line == '':
            continue
        if re.search(r'=', line):
            line = re.sub(r'\s+', '', line)
            source, destinations = line.split('=')
            nodes[source] = re.sub(r'\(|\)|\n', '', destinations).split(',')
        else:
            directions = line
    
    return directions, nodes


def main():

    directions, nodes = parse_input("8input.txt")

    print(directions)
    print(nodes)

    next_nodes, current_nodes = []

    for node in nodes:
        if node[2] == 'A':
            current_nodes.append(node)
    i = 0

    done = False

    while done == False:
        direction = ['L', 'R'].index(directions[i % len(directions)])
        for node in current_nodes:

        i += 1

    print("Total is: %s" % (i))
    #     print(hand[0], parse_hand(hand[0]))


if __name__ == "__main__":
    main()