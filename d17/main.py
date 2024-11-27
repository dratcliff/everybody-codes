from math import prod
from collections import defaultdict, deque
import heapq
from collections import deque
from itertools import combinations
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

stars = []
for y in range(H):
    for x in range(W):
        if G[(x, y)] == '*':
            stars.append((x, y))


def prim_mst(coords_graph):
    mst = []
    visited = set()
    total_weight = 0

    start = next(iter(coords_graph))
    min_heap = [(0, None, start)]  # (weight, from_coord, to_coord)

    while len(visited) < len(coords_graph):
        weight, from_coord, to_coord = heapq.heappop(min_heap)
        if to_coord in visited:
            continue

        visited.add(to_coord)
        if from_coord is not None:
            mst.append((from_coord, to_coord, weight))
            total_weight += weight

        for neighbor, edge_weight in coords_graph[to_coord]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, to_coord, neighbor))

    return mst, total_weight


def p1():
    coords_graph = {}
    for c in combinations(stars, 2):
        left = c[0]
        right = c[1]
        dist = abs(left[0]-right[0]) + abs(left[1]-right[1])
        if left not in coords_graph:
            coords_graph[left] = []
        if right not in coords_graph:
            coords_graph[right] = []
        coords_graph[left].append((right, dist))
        coords_graph[right].append((left, dist))

    mst, total_weight = prim_mst(coords_graph)
    star_set = set()
    for left, right, dist in mst:
        star_set.add(left)
        star_set.add(right)

    print("answer", total_weight+len(star_set))


def manhattan(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def partition_coords(coords, max_distance):
    graph = defaultdict(list)
    for i, coord1 in enumerate(coords):
        for j, coord2 in enumerate(coords):
            if i != j and manhattan(coord1, coord2) <= max_distance:
                graph[coord1].append(coord2)
                graph[coord2].append(coord1)

    visited = set()
    groups = []

    def bfs(start):
        queue = deque([start])
        component = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                component.append(node)
                queue.extend(graph[node])
        return component

    for coord in coords:
        if coord not in visited:
            group = bfs(coord)
            groups.append(group)

    return groups


sizes = []
groups = partition_coords(stars, 5)
for stars in groups:
    if len(stars) < 2:
        continue
    coords_graph = {}
    for c in combinations(stars, 2):
        left = c[0]
        right = c[1]
        dist = abs(left[0]-right[0]) + abs(left[1]-right[1])
        if left not in coords_graph:
            coords_graph[left] = []
        if right not in coords_graph:
            coords_graph[right] = []
        coords_graph[left].append((right, dist))
        coords_graph[right].append((left, dist))

    mst, total_weight = prim_mst(coords_graph)
    star_set = set()
    for left, right, dist in mst:
        star_set.add(left)
        star_set.add(right)
    answer = total_weight+len(star_set)
    sizes.append(answer)

sizes = list(sorted(sizes))[-3:]
print(prod(sizes))
