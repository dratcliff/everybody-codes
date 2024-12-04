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


xs = get_lines('p3.txt')
print(xs)

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
    'L': [
        'L', 'D', 'U'
    ],
    'R': [
        'R', 'D', 'U'
    ],
    'U': [
        'U', 'L', 'R'
    ]
}


def search(start_pt, altitude, D):
    best = None
    best2 = None
    best3 = None
    res = []
    i = 0
    Q = []
    startD = (start_pt, altitude, D, 0, start_pt)
    heapq.heappush(Q, (0, startD))
    visited = {}
    while Q:
        priority, (cur, alt, direction, time, cur_real) = heapq.heappop(Q)
        # print("!", priority, cur, cur_real, alt, direction, time, len(Q))
        if (direction, cur_real) in visited and alt <= visited[(direction, cur_real)]:
            # print(",", cur_real, direction, alt, visited[(direction, cur_real)])
            continue
        visited[(direction, cur_real)] = alt
        south = cur_real[1]
        diff = south - alt
        if best2 is None or diff > best2:
            best2 = diff
            # print("new best2", best2, time, alt)
        if alt <= 0:
            if best is None or south > best:
                best = south
                best3 = (direction, cur_real)
                # print("new one", cur_real, alt, direction, time)
            continue
        for move in moves[direction]:
            x1, y1 = move_offsets[move]
            x, y = cur
            nxt = ((x+x1), (y+y1) % H)
            nx, ny = cur_real
            nxt_real = (nx+x1, ny+y1)
            # print(cur, nxt_real[1]*-1, nxt, nxt_real, G[nxt], direction, move, alt)
            nxt_alt = alt
            if nxt in G:
                nxt_val = G[nxt]
                if nxt_val == '#':
                    continue
                elif nxt_val in ('.', 'S'):
                    nxt_alt -= 1
                elif nxt_val == '-':
                    nxt_alt -= 2
                elif nxt_val == '+':
                    nxt_alt += 1
                else:
                    continue
                nxt_item = (nxt, nxt_alt, move, time+1, nxt_real)
                heapq.heappush(Q, (nxt_real[1]*-1, nxt_item))
    print(altitude, best, best3)

# for i in range(100):
#     search(S, i, 'D')


def calc(i):
    if i % 2 == 0:
        return i*2 - 5
    else:
        return i*2 - 6


print(calc(384400))
