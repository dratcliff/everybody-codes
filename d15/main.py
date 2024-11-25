from itertools import product, permutations
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


CACHE = {}


def calc(G, start_pt, end_pt):
    if (start_pt, end_pt) in CACHE:
        return CACHE[(start_pt, end_pt)]
    if (end_pt, start_pt) in CACHE:
        return CACHE[(end_pt, start_pt)]
    Q = deque()
    visited = set()
    hd = 0
    Q.append((start_pt, 0))
    while Q:
        cur, dist = Q.popleft()
        if cur in visited:
            continue
        visited.add(cur)
        if cur == end_pt:
            CACHE[(start_pt, end_pt)] = dist
            return dist
        for x, y in OFFSETS:
            nxt = (cur[0]+x, cur[1]+y)
            if nxt not in visited and nxt in G and G[nxt] not in ('#', '~'):
                Q.append((nxt, dist+1))
    return None


# Generate all combinations
combinations = list(product(*LETTERS.values()))


# Generate all key combinations
key_combinations = combinations(data.keys(), 2)

# Generate all pairs for each key combination
all_pairs = {}
for key1, key2 in key_combinations:
    pairs = list(product(data[key1], data[key2]))
    all_pairs[(key1, key2)] = pairs

# Print the results
for keys, pairs in all_pairs.items():
    print(f"Combinations for keys {keys}:")
    for pair in pairs:
        print(pair)
    print()

# min_dist = float('infinity')
# for combination1 in combinations:

#     for combination in permutations(combination1):
#         dist = 0
#         # print("!!!", combination)
#         combination = (START,) + combination + (START,)
#         for i in range(len(combination)-1):
#             D = calc(G, combination[i], combination[i+1])
#             # print(combination, combination[i], combination[i+1], D)
#             dist += D
#         if dist < min_dist:
#             print("!", dist)
#             min_dist = dist
# print(len(combinations))
# print(calc(G, START, 'A'))

# from itertools import permutations

# for p in permutations(LETTERS):
#     print(p)
