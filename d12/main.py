from math import ceil
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


coords = get_lines('p3.txt')
coords = [(x.split()[0], x.split()[1]) for x in coords]
coords = [(int(x[0]), int(x[1])) for x in coords]
print(coords)
A = None
B = None
C = None
T = []

A = (0, 0)
B = (0, 1)
C = (0, 2)
# shooting power * 3 + d_y = d_x
# print(A, B, C, T)
powers = {
    A: 1,
    B: 2,
    C: 3
}
# s = 0
# for t in T:
#     for e in (A, B, C):
#         d_x = t[0]-e[0]
#         d_y = t[1]-e[1]
#         for i in range(100):
#             if i*3 + d_y == d_x:
#                 multiplier = 1
#                 if t[2] == 'H':
#                     multiplier = 2
#                 s += (i*powers[e])*multiplier
#                 break


def calc(tower, meteor_start, time, power):
    # print(tower, meteor_start, power)
    tx, ty = tower[0], tower[1]
    mx, my = meteor_start[0]-time, meteor_start[1]-time
    for i in range(power):
        tx += 1
        ty += 1
        mx -= 1
        my -= 1
        dist = abs(mx-tx) + abs(my-ty)
        # if dist < 2:
        #     print("tower", tower, meteor_start,(tx, ty), (mx, my), power, time)
        if mx == tx and my == ty:
            return (mx, my)
        if my < 0 or ty < 0:
            return None
    for j in range(power):
        tx += 1
        mx -= 1
        my -= 1
        dist = abs(mx-tx) + abs(my-ty)
        # if dist < 2:
        #     print("tower", tower, meteor_start,(tx, ty), (mx, my), power, time)
        if mx == tx and my == ty:
            return (mx, my)
        if my < 0 or ty < 0:
            return None
    k = 0
    while my > 0 and ty > 0:
        k += 1
        tx += 1
        ty -= 1
        mx -= 1
        my -= 1
        dist = abs(mx-tx) + abs(my-ty)
        # if dist < 2:
        #     print("tower", tower, meteor_start,(tx, ty), (mx, my), power, time)
        if mx == tx and my == ty:
            return (mx, my)
    return None


M = {}
s = 0
# slow, not optimized
for t in coords:
    hit2 = False
    for e in (A, B, C):
        # print(e,t)
        hit3 = False
        for t1 in range(2000):
            if hit3:
                break
            for i in range(1, 2000):
                # print(t, e, i)
                hit = calc(e, t, t1, i)
                if hit:
                    hit2 = True
                    if t not in M:
                        M[t] = (powers[e]*i, hit[1])
                        print("hit", i, e, t, t1, M[t][1])
                    elif hit[1] > M[t][1]:
                        M[t] = (powers[e]*i, hit[1])
                        print("hit", i, e, t, t1, M[t][1])
                    elif hit[1] == M[t][1] and powers[e]*i < M[t][0]:
                        M[t] = (powers[e]*i, hit[1])
                        print("hit", i)
                    hit3 = True
                    break
    if not hit2:
        print("not hit", t, i)


print(sum([x[0] for x in M.values()]))
