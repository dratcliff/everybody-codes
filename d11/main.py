xs = [x.strip('\n') for x in open('p3.txt').readlines()]
xs = [x.split(":") for x in xs]
xs = [[x[0], x[1].split(",")] for x in xs]
xs = {x[0]: x[1] for x in xs}
print(xs)

from collections import defaultdict



all_counts = defaultdict(int)

for each in xs.keys():
    counts = defaultdict(int)
    counts[each] = 1
    for i in range(20):
        new_counts = defaultdict(int)
        for f in counts.keys():
            for e in xs[f]:
                new_counts[e] += counts[f]
        counts = new_counts

    all_counts[each] = sum(counts.values())

small = min(all_counts.values())
big = max(all_counts.values())

print(big-small)


