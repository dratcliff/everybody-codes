OFFSETS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
OFFSETS_D = [(1, 0), (-1, 0), (0, -1), (0, 1),
             (1, 1), (1, -1), (-1, 1), (-1, -1)]

OFFSETS_CLOCKWISE = [
    (0, -1),   # Top
    (-1, -1),  # Top-left
    (-1, 0),   # Left
    (-1, 1),   # Bottom-left
    (0, 1),    # Bottom
    (1, 1),    # Bottom-right
    (1, 0),    # Right
    (1, -1),   # Top-right
]


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

instr = xs[0]

rest = xs[2:]

G, W, H = to_grid(rest)


def rotate(G, pt, dir):
    next_values = {}
    x, y = pt
    for i, (x1, y1) in enumerate(OFFSETS_CLOCKWISE):
        cur = (x+x1, y+y1)
        cur_val = G[cur]
        shift = 1 if dir == "L" else -1
        x2, y2 = OFFSETS_CLOCKWISE[(i+shift) % len(OFFSETS_CLOCKWISE)]
        nxt = (x+x2, y+y2)
        next_values[nxt] = cur_val
    for k, v in next_values.items():
        G[k] = v


def p(G):
    s = ""
    for y in range(H):
        for x in range(W):
            s += G[(x, y)]
        s += "\n"
    print(s)


index = 0
for y in range(1, H-1):
    for x in range(1, W-1):
        rotate(G, (x, y), instr[index % len(instr)])
        index += 1

p(G)
