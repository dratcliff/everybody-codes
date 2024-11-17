xs = [x.strip('\n') for x in open('p3.txt').readlines()]
xs = [x.split(":") for x in xs]
xs = [[x[0], x[1].split(",")] for x in xs]
T = {}
from collections import deque

for x in xs:
    root = x[0]
    paths = x[1]
    if root not in T:
        T[root] = []
    for p in paths:
        T[root].append(p)


Q = deque()
for t in T:
    Q.append((t, []))

while Q:
    (cur, path) = Q.popleft()
    if cur == '@' and 'RR' in path:
        print(''.join([x[0] for x in path + ['@']]))
        print(''.join(path + ['@']), len(path))
    else:
        if cur in T:
            for t in T[cur]:
                Q.append((t, path + [cur]))