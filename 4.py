
import functools
import re


def parse_input(filename):

    # points = 0

    card_count = []
    index = 0

    file = open(filename)
    for line in file.readlines():

        if (len(card_count) < index + 1):
            card_count.append(1)
        else:
            card_count[index] += 1

        parts = re.split(r':|\|', line.rstrip())
        lucky_numbers = filter(lambda n: n != '', parts[1].split(' '))
        actual_numbers = filter(lambda n: n != '', parts[2].split(' '))
        correct = len(set(lucky_numbers) & set(actual_numbers))
        
        for i in range(correct):
            if (len(card_count) <= index + i + 1):
                card_count.append(0)
            card_count[index + i + 1] += card_count[index]

        index += 1

    print(card_count)
    print(functools.reduce(lambda x, y: x + y, card_count[0:index]))

def main():
    points = parse_input('4input.txt')
    print("Total points is: %s" % (points))


if __name__ == "__main__":
    main()