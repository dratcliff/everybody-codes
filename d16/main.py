from math import lcm
from collections import Counter
OFFSETS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
OFFSETS_D = [(1, 0), (-1, 0), (0, -1), (0, 1),
             (1, 1), (1, -1), (-1, 1), (-1, -1)]


def to_grid(xs):
    H = len(xs)
    W = len(xs[0])
    G = {}
    for y in range(H):
        for x in range(W):
            G[(x, y)] = xs[y][x]

    return (G, W, H)


def get_lines(filename):
    return [x.strip('\n') for x in open(filename).readlines()]


xs = get_lines('p2.txt')

ps = xs[0]
ps = [int(x) for x in ps.split(',')]
print(ps)
wheel = {}
for i in xs[2:]:
    for j in range(0, len(ps)):
        if j not in wheel:
            wheel[j] = []
        entry = i[j*4:j*4+3]
        if " " not in entry and len(entry) > 0:
            wheel[j].append(entry)


L = []
for j in range(len(ps)):
    L.append(len(wheel[j]))
# print(L)
M = lcm(*L)

t1 = 0
for i in range(M):
    entry = ""
    for j in range(len(ps)):
        cat = wheel[j][(i+1)*ps[j] % len(wheel[j])]
        # print("!", cat, cat[0], cat[2])
        entry += cat[0] + cat[2]
    c = Counter(entry)
    t1 += sum([x-2 for x in c.values() if x >= 3])
    # print(i, t1, c, entry)

t2 = 0
for i in range(202420242024 % M):
    entry = ""
    for j in range(len(ps)):
        cat = wheel[j][(i+1)*ps[j] % len(wheel[j])]

        entry += cat[0] + cat[2]
    c = Counter(entry)
    t2 += sum([x-2 for x in c.values() if x >= 3])

print(t1*(202420242024//M) + t2, t2)
