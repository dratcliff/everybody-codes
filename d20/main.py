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


xs = get_lines('p1.txt')
print(xs)

"""
. == lose 1
-  == lose 2
+ == gain 1
"""

G, W, H = to_grid(xs)

S = None

for y in range(H):
    for x in range(W):
        if G[(x, y)] == 'S':
            S = (x, y)


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

D = 'D'


Q = deque()
visited = set()

Q.append((S, 'D', 1000, 0))

highest = None
while Q:
    (cur, direction, alt, time) = Q.pop()
    if highest == None or alt > highest:
        highest = alt
        print("new highest", highest)
    # print(cur, direction, alt, time)
    if (cur, direction, alt, time) in visited or time == 100:
        continue
    if highest and (100-time)+alt < highest:
        continue
    visited.add((cur, direction, alt, time))
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
            Q.append((nxt, move, nxt_alt, time+1))
