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
LETTERS = {}
for x in range(W):
    for y in range(H):
        if G[(x, y)] not in ('#', '.', '~', 'B', 'H', 'O', 'K'):
            letter = G[(x, y)]
            if letter not in LETTERS:
                LETTERS[letter] = []
            LETTERS[letter].append((x, y))

START = None
for x in range(W):
    if G[(x, 0)] == '.':
        START = (x, 0)


def calc(G, start_pt, end_pt):
    Q = deque()
    visited = set()
    Q.append((start_pt, 0))
    neighbors = {}
    letter_keys = LETTERS.keys()
    while Q:
        (cur, dist) = Q.popleft()

        if cur in visited:
            continue
        visited.add(cur)

        current_letter = G[cur]
        if current_letter in letter_keys or cur == START:
            if dist != 0:
                neighbors[cur] = dist
        for x, y in OFFSETS:
            nxt = (cur[0]+x, cur[1]+y)
            if nxt in G and G[nxt] not in ('#', '~'):
                Q.append((nxt, dist+1))

    return neighbors


GRAPH = {}

for letter in LETTERS.keys():
    for e in LETTERS[letter] + [START]:
        neighobrs = calc(G, e, None)
        # print(letter, e, neighobrs)
        for k, v in neighobrs.items():
            # print(",", letter, e, G[e], k, G[k], v)
            if e not in GRAPH:
                GRAPH[e] = {}
            if k not in GRAPH:
                GRAPH[k] = {}
            if k not in GRAPH[e] or v < GRAPH[e][k]:
                GRAPH[e][k] = v
            if e not in GRAPH[k] or v < GRAPH[k][e]:
                GRAPH[k][e] = v


def calc2(G, GRAPH, start_pt):
    Q = deque()
    best_results = {}
    Q.append((start_pt, 0, []))
    best_distance = None
    closest = {}
    to_find = len(LETTERS.keys())+1
    while Q:
        (cur, dist, found) = Q.pop()
        if best_distance and dist >= best_distance:
            continue
        found_ct = len(found)
        if dist > 0 and G[cur] == '.' and found_ct < to_find:
            continue
        found_letters = tuple(sorted(found + [G[cur]]))
        if cur not in best_results:
            best_results[cur] = {}
        if found_letters not in best_results[cur] or dist < best_results[cur][found_letters]:
            best_results[cur][found_letters] = dist
        else:
            if len(found_letters) > 0:
                continue

        if found_ct == to_find and G[cur] == '.':
            print("!", cur, dist, found)
            if best_distance == None or dist < best_distance:
                best_distance = dist
        options = {}
        if cur in closest:
            options = closest[cur]
        else:
            for (pos, dist1) in GRAPH[cur].items():
                letter = G[pos]
                if letter not in options or dist1 < options[letter][1]:
                    options[letter] = (pos, dist1)
            closest[cur] = options

        for letter, (pos, dist1) in options.items():
            if found_ct+1 != to_find and letter == '.':
                continue
            if letter not in found and (best_distance is None or dist+dist1 < best_distance):
                Q.append((pos, dist+dist1, found + [letter]))
    return None


calc2(G, GRAPH, START)
