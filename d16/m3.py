import heapq
from collections import deque
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


xs = get_lines('p3.txt')

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

Q = []
# Q.append()
heapq.heappush(Q, (0, ((0,)*len(ps), 0, 0)))
smallest = {}
G = {}
while Q:
    priority, (offsets, round, won) = heapq.heappop(Q)
    if offsets not in G:
        G[offsets] = []
    if round == 256:
        continue
    else:
        for O in (-1, 0, 1):
            nxt_offsets = []
            entry = ""
            for j in range(len(ps)):
                nxt = (offsets[j]+O) % len(wheel[j])
                nxt = (nxt+ps[j]) % len(wheel[j])
                nxt_offsets.append(nxt)
                cat = wheel[j][nxt]
                entry += cat[0] + cat[2]
            c = Counter(entry)
            won2 = sum([x-2 for x in c.values() if x >= 3])
            t = tuple(nxt_offsets)

            if (t, won2) not in G[offsets]:
                print("new one", offsets, t, won2)
                G[offsets].append((t, won2))
                smallest[(t, won2)] = True
                heapq.heappush(
                    Q, (won+won2, (tuple(nxt_offsets), round+1, won+won2)))

Q = []
heapq.heappush(Q, (0, (0, 0, (0,)*len(ps))))
smallest = None
largest = None
visited = set()
while Q:
    priority, (round, won, pos) = heapq.heappop(Q)
    if (round, won, pos) in visited:
        continue
    visited.add((round, won, pos))
    if round == 256:
        if not smallest or won < smallest:
            smallest = won
            print(largest, smallest)
        if not largest or won > largest:
            largest = won
            print(largest, smallest)
    else:
        for neighbor, winnings in G[pos]:
            heapq.heappush(
                Q, (-10*(round+1), (round+1, won+winnings, neighbor)))

print(largest, smallest)
