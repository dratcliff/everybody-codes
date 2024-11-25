from itertools import combinations
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
# print(xs)

G, W, H = to_grid(xs)
LETTERS = {}
for x in range(W):
    for y in range(H):
        if G[(x, y)] not in ('#', '.', '~'):
            letter = G[(x, y)]
            if letter not in LETTERS:
                LETTERS[letter] = []
            LETTERS[letter].append((x, y))

START = None
for x in range(W):
    if G[(x, 0)] == '.':
        START = (x, 0)


# for each a given start_pt, find all
# neighbors
"""
{
  (x1,y1): c1,
  (x2,y2): c2
}

"""


def calc(G, start_pt, end_pt):
    Q = deque()
    visited = set()
    hd = 0
    Q.append((start_pt, 0))
    neighbors = {}
    start_letter = G[start_pt]
    while Q:
        (cur, dist) = Q.popleft()
        # print(start_pt, cur, dist)

        if cur in visited:
            continue
        visited.add(cur)

        current_letter = G[cur]
        if current_letter in LETTERS.keys() or cur == START:
            if dist != 0:
                neighbors[cur] = dist
        for x, y in OFFSETS:
            nxt = (cur[0]+x, cur[1]+y)
            # print("o", start_pt, cur, nxt)
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

NG = {}
for c in combinations(list(LETTERS.keys()) + [G[START]], 2):
    left = c[0]
    right = c[1]
    print("!!!", left, right)
    min_pair = None
    LEFT = [START] if left not in LETTERS else LETTERS[left]
    RIGHT = [START] if right not in LETTERS else LETTERS[right]
    for e in LEFT:
        for f in RIGHT:
            # print("left", left, e, "right", right, f)
            if left not in NG:
                NG[left] = {}
            if right not in NG:
                NG[right] = {}

            left_right = GRAPH[e][f]
            # print(e, f, left_right, NG)
            if right not in NG[left] or left_right < NG[left][right][1]:
                NG[left][right] = ((e, f), left_right)
            if left not in NG[right] or left_right < NG[right][left][1]:
                NG[right][left] = ((f, e), left_right)


for k, v in GRAPH.items():
    print("kv", k, v)

NG2 = {}

for k, v in NG.items():
    for v2 in v.values():
        a = v2[0]
        left = a[0]
        right = a[1]
        dist = v2[1]
        if left not in NG2:
            NG2[left] = {}
        NG2[left][right] = dist
        if right not in NG2:
            NG2[right] = {}
        NG2[right][left] = dist

for k, v in NG2.items():
    print("kv2", k, v)

# GRAPH = NG2

"""
what's the "best" result at a position?
if we have been to a position before with the same letters found and a lower distance, we shouldn't continue
{
 (x,y): ('A', 'B')
}

"""


def calc2(G, GRAPH, start_pt):
    Q = []
    visited = {}
    best_results = {}
    best_to_find = {}
    hd = 0
    heapq.heappush(Q, (0, (start_pt, 0, [])))
    best_distance = None
    while Q:
        priority, (cur, dist, found) = heapq.heappop(Q)
        # print(cur, dist, found, G[cur])
        if best_distance and dist > best_distance:
            continue
        found_ct = len(set(found))
        if dist > 0 and G[cur] == '.' and found_ct < len(LETTERS.keys()) + 1:
            continue
        found_letters = tuple(sorted(set(tuple(found + [G[cur]]))))
        if cur not in best_results:
            best_results[cur] = {}
        if found_letters not in best_results[cur] or dist < best_results[cur][found_letters]:
            best_results[cur][found_letters] = dist
        else:
            if len(found_letters) > 0:
                continue

        if found_ct > hd:
            hd = found_ct
            print("!!", hd, cur, dist, found, len(Q))
        if found_ct == len(LETTERS.keys())+1 and G[cur] == '.':
            print("!", cur, dist, found, len(Q))
            if best_distance == None or dist < best_distance:
                best_distance = dist
        # visited.add(cur)
        # print(GRAPH[cur])
        options = {

        }
        for (pos, dist1) in GRAPH[cur].items():
            letter = G[pos]
            # if letter not in found:
            heapq.heappush(Q, (-10000*found_ct+(dist+dist1),
                           (pos, dist+dist1, found + [letter])))
    return None


# TO_START = {START: 0}
# for k in GRAPH[START]:
#     for k1 in GRAPH[START][k]:
#         for pt in GRAPH[START][k][k1]:
#             if pt not in TO_START or k1 < TO_START[pt]:
#                 TO_START[pt] = k1

print(LETTERS)
calc2(G, GRAPH, START)

# for k, v in GRAPH.items():
#     n = set()
#     for v1 in v:
#         n.add(G[v1])
#     print(k, n, len(n))
