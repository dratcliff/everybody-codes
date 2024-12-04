from itertools import product
import heapq
from collections import deque
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
# print(xs)

"""
. == lose 1
-  == lose 2
+ == gain 1
"""

G, W, H = to_grid(xs)

S = None
A = None
B = None
C = None

for y in range(H):
    for x in range(W):
        if G[(x, y)] == 'S':
            S = (x, y)
        if G[(x, y)] == 'A':
            A = (x, y)
        if G[(x, y)] == 'B':
            B = (x, y)
        if G[(x, y)] == 'C':
            C = (x, y)

move_offsets = {
    'D': (0, 1),
    'U': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}

moves = {
    'D': [
        'D', 'L', 'R'
    ],
    'U': [
        'U', 'L', 'R'
    ],
    'L': [
        'L', 'U', 'D'
    ],
    'R': [
        'R', 'U', 'D'
    ]
}


def search(start_pt, end_pt, D, target=None):
    res = []
    i = 0
    Q = []
    start_letter = G[start_pt]
    end_letter = G[end_pt]
    highest = {}
    visited = {}
    startD = (start_pt, D, D, 0, 0)
    heapq.heappush(Q, (0, startD))
    done = False
    while Q and not done:
        i += 1
        if i % 100000 == 0 and len(res) > 0:
            print(i, res[-1][0])
        priority, (cur, start_direction, direction,
                   alt, time) = heapq.heappop(Q)
        if (direction, cur) in visited and alt <= visited[(direction, cur)]:
            continue
        visited[(direction, cur)] = alt
        if cur == end_pt:
            if (target and alt >= target) or (target is None and len(highest) > 1):
                done = True
            response = (f"{start_letter} -> {end_letter} time {time} altitude {alt}",
                        time, alt, start_direction, direction)
            # print(response, len(Q))
            res.append(response)
            continue

        options = []
        for move in moves[direction]:
            x1, y1 = move_offsets[move]
            x, y = cur
            nxt = (x+x1, y+y1)
            if nxt in G and G[nxt] != '#':
                options.append(nxt)
        for move in moves[direction]:
            x1, y1 = move_offsets[move]
            x, y = cur
            nxt = (x+x1, y+y1)
            nxt_alt = alt
            if nxt in G:
                nxt_val = G[nxt]
                if nxt_val == '#':
                    continue
                elif nxt_val == '.':
                    nxt_alt -= 1
                elif nxt_val == '-':
                    nxt_alt -= 2
                elif nxt_val == '+':
                    nxt_alt += 1
                elif nxt_val == end_letter:
                    nxt_alt -= 1
                else:
                    continue
                first_move = move if start_direction is None else start_direction
                nxt_item = (nxt, first_move, move, nxt_alt, time+1)
                heapq.heappush(Q, (time+1, nxt_item))

    return res


SA = (0, -1*float('infinity'))
SAs = {}
AB = (0, -1*float('infinity'))
ABs = {}
BC = (0, -1*float('infinity'))
BCs = {}
CS = (0, -1*float('infinity'))
CSs = {}

for i in search(S, A, D='D', target=10):
    # print("!", i)
    msg, time, alt, start_direction, direction = i
    key = time
    if key not in SAs or alt > SAs[key][0]:
        SAs[key] = (alt, start_direction, direction)
        # print(i)

# for k, v in SAs.items():
#     print("SA", k, v)

for i in search(A, B, D='D', target=10):
    # print("!!", i)
    msg, time, alt, start_direction, direction = i
    key = time
    if key not in ABs or alt > ABs[key][0]:
        ABs[key] = (alt, start_direction, direction)
        # print(i)

# for k, v in ABs.items():
#     print("AB", k, v)

for i in search(B, C, D='U', target=10):
    # print("!!!", i)
    msg, time, alt, start_direction, direction = i
    key = time
    if key not in BCs or alt > BCs[key][0]:
        BCs[key] = (alt, start_direction, direction)
        # print(i)

# for k, v in BCs.items():
#     print("BC", k, v)

for i in search(C, S, D='R', target=100):
    msg, time, alt, start_direction, direction = i
    key = time
    if key not in CSs or alt > CSs[key][0]:
        CSs[key] = (alt, start_direction, direction)
        # print(i)

# for k, v in CSs.items():
#     print("CS", k, v)

best = None
for k, (alt, sd, d) in SAs.items():
    # print("alt", alt, sd, d)
    for k1, (alt1, sd1, d1) in ABs.items():
        # print("alt1", alt1, sd1, d1)
        for k2, (alt2, sd2, d2) in BCs.items():
            for k3, (alt3, sd3, d3) in CSs.items():
                alt4 = alt+alt1+alt2+alt3
                time = k+k1+k2+k3
                if alt4 >= 0:
                    if best is None or time < best[0]:
                        best = (time, alt4)
                        print("new best", best, sd, d,
                              sd1, d1, sd2, d2, sd3, d3)
