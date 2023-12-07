import functools
import re

class Interval:
    range = []
    delta = 0

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.range) + " " +  str(self.delta)

def parse_input(filename):

    seeds = []
    mappings = {}

    file = iter(open(filename).readlines())
    for line in file:
        line = line.rstrip()
           
        if re.search(r'seeds:', line):
            seeds = list(filter(lambda x: x != '', line.split(':')[1].split(' ')))
            seeds = list(map(lambda x: int(x), seeds))
        if re.search(r'map', line):
            parts = re.split('-|\s', line)
            nextline = next(file)
            mappings[parts[0]] = []
            while nextline != '\n':
                mappings[parts[0]].append(list(map(lambda x: int(x), nextline.rstrip().split(' '))))
                try:
                    nextline = next(file)
                except Exception:
                    break

    return seeds, mappings

def overlaps(rangeA, rangeB):
    return rangeA[0] < rangeB[1] and rangeA[1] > rangeB[0]

def build_mappings(mappings):

    existing_intervals = []

    for mapping in mappings:

        map_intervals = []

        for map_details in mappings[mapping]:

            interval = Interval()
            interval.range = [map_details[1], map_details[1] + map_details[2]]
            interval.delta = map_details[0] - map_details[1]
            
            map_intervals.append(interval)
            
        numbers = functools.reduce(lambda a, b: a + b.range, map_intervals, [])
        numbers += functools.reduce(lambda a, b: a + [b.range[0] + b.delta, b.range[1] + b.delta], existing_intervals, [])
        numbers = list(set(numbers)) # eliminate dupes
        numbers.sort()

        new_intervals = []

        for i in range(len(numbers) - 1):
            interval = Interval()
            interval.range = [numbers[i], numbers[i + 1]]
            for map_interval in map_intervals:
                if overlaps(interval.range, map_interval.range):
                    interval.delta = map_interval.delta

            new_intervals.append(interval)

        for ni in new_intervals:

            for ei in existing_intervals:
                if overlaps(ni.range, list(map(lambda x: x + ei.delta, ei.range))):
                    ni.delta += ei.delta
                    ni.range[0] -= ei.delta
                    ni.range[1] -= ei.delta
                    break

        existing_intervals = new_intervals

    return existing_intervals

def map_seed(seed, intervals):
    for interval in intervals:
        if seed in range(interval.range[0], interval.range[1]):
            return seed + interval.delta
    
    return seed

def main():

    min_location = -1

    seeds, mappings = parse_input('5input.txt')

    mappings = build_mappings(mappings)
    i = 0

    numbers = []
    seed_intervals = []

    while i < len(seeds):

        interval = [seeds[i], seeds[i] + seeds[i + 1]]
        seed_intervals.append(interval)

        i += 2

    for seed_interval in seed_intervals:
        for mapping in mappings:
            if overlaps(seed_interval, mapping.range):
                if min_location > mapping.range[0] + mapping.delta or min_location == -1:
                    min_location = mapping.range[0] + mapping.delta
                    print("seed %s => loc %s" % (mapping.range[0], mapping.range[0] + mapping.delta))

    print("Min location is : %s" % (min_location))

if __name__ == "__main__":
    main()