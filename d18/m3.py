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
# print(xs)


G, W, H = to_grid(xs)


ps2 = set()
for (x, y), v in G.items():
    # print(x,y,v)
    if v == 'P':
        ps2.add((x, y))

spots = [(x, y) for (x, y), v in G.items() if v == '.']
print(spots)

best_spot = None
for i, spot in enumerate(spots):
    wait_times = 0
    visited = set()
    Q = deque()
    Q.append((spot, 0))
    ps = ps2.copy()
    while Q:
        (x, y), dist = Q.popleft()
        if best_spot and dist > best_spot:
            continue
        # print(x, y, dist, ps)
        if (x, y) not in visited:
            visited.add((x, y))
            if (x, y) in ps:
                ps.remove((x, y))
                wait_times += dist
            if len(ps) == 0:
                # print(dist)
                if best_spot is None or wait_times < best_spot:
                    best_spot = wait_times
                    print("new best", best_spot, i, len(spots))
            for x1, y1 in OFFSETS:
                nxt = (x+x1, y+y1)
                if nxt in G and G[nxt] != '#' and len(ps) > 0:
                    Q.append((nxt, dist+1))
