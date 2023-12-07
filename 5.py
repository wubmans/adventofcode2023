import re

class Interval:
    range = []
    delta = 0

    def translated(self):
        translatedInterval = Interval()
        translatedInterval.delta = self.delta
        translatedInterval.range = [self.range[0] + self.delta, self.range[1]+ self.delta]
        return translatedInterval
    
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.range) + " < " +  str(self.delta)

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
            # print(next(file))

    return seeds, mappings

def create_intersection(intervalA, intervalB):
    points = list(set(intervalA.range + intervalB.range))
    points.sort()

    intervals = []
   
    for i in range(0, len(points) - 1):
 
        interval = Interval()
        interval.range = [points[i], points[i + 1]]
        
        if intersects(interval, intervalA):
            interval.delta += intervalA.delta
        
        if intersects(interval, intervalB):
            interval.delta += intervalB.delta
            interval.range[0] -= intervalB.delta
            interval.range[1] -= intervalB.delta
        
        intervals.append(interval)

    return intervals

def intersects(intervalA, intervalB):
    return (intervalA.range[1] > intervalB.range[0] and intervalA.range[0] < intervalB.range[1])


def shift(range, delta, unshift = False):
    if unshift == True:
        return [range[0] - delta, range[1] - delta]
    else:
        return [range[0] + delta, range[1] + delta]

def build_mappings(mappings):

    result_intervals = []

    for mapping in mappings:

        new_intervals = []

        for map in mappings[mapping]:

            interval = Interval()
            interval.range = [map[1], map[1] + map[2]]
            interval.delta = map[0] - map[1]
            
            if len(result_intervals) == 0:
                new_intervals.append(interval)

            else:

                intersected = False

                for i in result_intervals:

                    if intersects(interval, i.translated()):
                        sliced_intervals = create_intersection(interval, i.translated())
                        new_intervals += sliced_intervals
                        intersected = True

                if intersected == False:
                        new_intervals.append(interval)


        result_intervals = new_intervals   

    return result_intervals

def map_seed(seed, intervals):
    for interval in intervals:
        intervalrange = interval.translated().range
        if seed in range(intervalrange[0], intervalrange[1]):
            return seed + interval.delta
    
    return seed

def main():

    min_location = -1

    seeds, mappings = parse_input('5input.txt')

    mappings = build_mappings(mappings)
    i = 0

    while i < len(seeds):

        seed = seeds[i]
        r = seeds[i + 1]
        for s in range(seed, seed + r):
            mapped_seed = map_seed(s, mappings)
            if mapped_seed < min_location or min_location == -1:
                min_location = mapped_seed

        i += 2

    print(map_seed(82,  mappings))
    print("the lowest location: %s" % (min_location))

if __name__ == "__main__":
    main()