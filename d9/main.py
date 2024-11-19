xs = [x.strip('\n') for x in open('p3.txt').readlines()]
xs = [int(x) for x in xs]
dots = list(reversed([1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]))
# dots = list(reversed([1, 3, 5, 10, 15, 16, 20, 24, 25, 30]))
from itertools import combinations_with_replacement
m = {}
m[0] = 0
for i in range(1, 14):
    for c in combinations_with_replacement(dots, i):
        s = sum(c)
        if s not in m:
            m[s] = i
        else:
            m[s] = min(m[s], i)

def combinations_within_range(target, tolerance=100):
    for a in range(target//2 - 101, target//2 + 101):
        for b in range(target//2 - 101, target//2 + 101):
            if a + b == target and abs(a-b) <= tolerance:
                yield (a,b)


def split(x):
    M = None
    start = x // 2
    start -= 1
    for k, v in m.items():
        new_num = x-k
        if new_num % dots[0] == 0:
            maybe = int(new_num // dots[0]) + v
            if M is None or maybe < M:
                M = maybe
    return M

T = 0
for x in xs:
    B = None
    for e in combinations_within_range(x):
        first = split(e[0])
        second = split(e[1])
        s = first + second
        if B is None or s < B:
            print(x, e, first, second, s)
            B = s
    T += B

print(T)

