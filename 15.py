import re


file = open('15input.txt')
boxes = [{} for i in range(256)]

for line in file:
    parts = line.split(',')
    total = 0
    for part in parts:
        label, focus = re.split(r'-|=', part)
        
        s = 0
        for i in label:
            s += ord(i)
            s *= 17
            s %= 256
        print(s)
       
        # if label not in boxes[s]:
        #     continue

        if '-' in part:
            if label in boxes[s]:
                boxes[s].pop(label)
        else:
            boxes[s][label] = focus

total = 0

for s in range(len(boxes)):
    for i, k in enumerate(boxes[s]):
        print(s, k, boxes[s][k], (i + 1), (s + 1) * (i + 1) * int(boxes[s][k]))
        total += (s + 1) * (i + 1) * int(boxes[s][k])

print(total)
