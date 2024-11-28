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

visited = set()


G, W, H = to_grid(xs)


ps = set()
for (x, y), v in G.items():
    # print(x,y,v)
    if v == 'P':
        ps.add((x, y))

Q = deque()
Q.append(((0, 1), 0))
Q.append(((200, 69), 0))
while Q:
    (x, y), dist = Q.popleft()
    # print(x, y, dist, ps)
    if (x, y) not in visited:
        visited.add((x, y))
        if (x, y) in ps:
            ps.remove((x, y))
        if len(ps) == 0:
            print(dist)
        for x1, y1 in OFFSETS:
            nxt = (x+x1, y+y1)
            if nxt in G and G[nxt] != '#' and len(ps) > 0:
                Q.append((nxt, dist+1))
