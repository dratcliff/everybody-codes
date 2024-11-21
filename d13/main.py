import heapq
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
G, W, H = to_grid(xs)
SS = []
E = None

for y in range(H):
    for x in range(W):
        if G[(x, y)] == 'S':
            SS.append((x, y))
        elif G[(x, y)] == 'E':
            E = (x, y)

best_paths = {}
Q = []
heapq.heappush(Q, (0, (E, [])))
least = None
while Q:
    priority, (cur, path) = heapq.heappop(Q)
    if G[cur] == 'S' and (least is None or priority < least):
        least = priority
        print(least)
        break
    for O in OFFSETS:
        nxt = (cur[0]+O[0], cur[1]+O[1])
        if nxt in G and G[nxt] not in ('#', ' ') and nxt not in path:
            s = 0
            p = G[cur]
            n = G[nxt]
            v = 0 if p in ('S', 'E') else p
            v1 = 0 if n in ('S', 'E') else n
            cost = abs(int(v)-int(v1))
            if cost > 5:
                cost = 10 - cost
            s += priority + cost + 1
            if (cur, nxt) not in best_paths or s < best_paths[(cur, nxt)]:
                best_paths[(cur, nxt)] = s
                heapq.heappush(Q, (s, (nxt, path + [cur])))
