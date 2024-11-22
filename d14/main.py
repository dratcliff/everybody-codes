from collections import deque
OFFSETS = [(x, y, z) for x in range(-1, 2)
           for y in range(-1, 2) for z in range(-1, 2)]
OFFSETS = [(x, y, z) for (x, y, z) in OFFSETS if (x, y, z).count(0) == 2]


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
xs = [x.split(',') for x in xs]
xs = [[[y[0], int(y[1:])] for y in x] for x in xs]

mx = 0
my = 0
mz = 0
G = {}
L = {}
for zz in xs:
    x1 = 0
    y1 = 0
    z1 = 0
    for x in zz:
        if x[0] == 'U':
            for m in range(x[1]):
                y1 += 1
                G[(x1, y1, z1)] = True
        elif x[0] == 'D':
            for m in range(x[1]):
                y1 -= 1
                G[(x1, y1, z1)] = True
        elif x[0] == 'L':
            for m in range(x[1]):
                x1 -= 1
                G[(x1, y1, z1)] = True
        elif x[0] == 'R':
            for m in range(x[1]):
                x1 += 1
                G[(x1, y1, z1)] = True
        elif x[0] == 'F':
            for m in range(x[1]):
                z1 -= 1
                G[(x1, y1, z1)] = True
        elif x[0] == 'B':
            for m in range(x[1]):
                z1 += 1
                G[(x1, y1, z1)] = True
        mx = max(x1, mx)
        my = max(y1, my)
        zy = max(z1, mz)
        G[(x1, y1, z1)] = True
    L[(x1, y1, z1)] = True


def calc(G, L, t):
    Q = deque()
    visited = set()
    leaf_dist = 0
    Q.append((t, 0))
    while Q:
        cur, dist = Q.popleft()
        if cur in visited:
            continue
        visited.add(cur)
        if cur in L:
            leaf_dist += dist
        for x, y, z in OFFSETS:
            nxt = (cur[0]+x, cur[1]+y, cur[2]+z)
            if nxt not in visited and nxt in G:
                Q.append((nxt, dist+1))
    return leaf_dist


smallest_murkiness = float('infinity')
trunk = [x for x in G.keys() if x[0] == 0 and x[2] == 0]
for t in trunk:
    smallest_murkiness = min(smallest_murkiness, calc(G, L, t))

print(smallest_murkiness)
