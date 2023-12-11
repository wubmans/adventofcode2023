from math import floor
from functools import cmp_to_key
import re


def parse_input(filename):


    data = []
    
    file = iter(open(filename).readlines())
    for line in file:
        line = line.rstrip()
        data.append(line.split(' '))
    
    return data

def parse_hand(hand):

    sets = {}
    
    for i in range(5):
        if hand[i] in sets:
            sets[hand[i]] += 1
        else:
            sets[hand[i]] = 1


    if "J" in hand:
        max_rank = -1
        new_hand = None

        for i in sets:

            rank = parse_hand(hand.replace("J", i))
            if max_rank == -1 or rank > max_rank:
                new_hand = hand.replace("J", i)
                max_rank = rank

        return max_rank

    if len(sets) == 1:
        return 1 # five-of-a-kind
    if len(sets) == 2:
        if 4 in sets.values():
            return 2 # four-of-a-kind
        else:
            return 3 # full house
    if len(sets) == 3:
        if 3 in sets.values():
            return 4  # three-of-a-kind
        else:
            return 5 # two pair
    
    if len(sets) == 4:
        return 6 # one pair
    
    return 7 # high card

    print(len(sets))

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', '1']

def sort_hands(handA, handB):
    rankA = parse_hand(handA[0])
    rankB = parse_hand(handB[0])

    if (rankA != rankB):
        return -1 if rankA > rankB else 1

    for i in range(5):
        if handA[0][i] != handB[0][i]:
            return - 1 if cards.index(handA[0][i]) > cards.index(handB[0][i]) else 1

def main():

    data = parse_input("7input.txt")

    data = sorted(data, key=cmp_to_key(sort_hands))

    print(data)

    total = 0

    for i in range(len(data)):
        total += (i + 1) * int(data[i][1])


    print("Total is: %s" % (total))
    #     print(hand[0], parse_hand(hand[0]))


if __name__ == "__main__":
    main()