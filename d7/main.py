xs = [x.strip('\n') for x in open('p2.txt').readlines()]
xs = [x.split(":") for x in xs]
xs = {x[0]: x[1].split(",") for x in xs}

ts = [x.strip('\n') for x in open('p2-track.txt').readlines()]
ts = [ts[0] + ''.join([x[-1] for x in ts[1:-1]]) + ''.join(reversed(ts[-1])) + ''.join([x[0] for x in ts[-2:0:-1]])][0]
print(ts)

gathered = {k: 0 for k in xs.keys()}
power = {k: 10 for k in xs.keys()}

for k, v in xs.items():
    p = power[k]
    e = gathered[k]
    for i in range(10*len(ts)):
        op = v[i % len(v)]
        override = ts[(i+1)%len(ts)]
        if override == '+':
            p += 1
        elif override == '-':
            p -=1
        elif op == '+':
            p += 1
        elif op == '-':
            p -= 1
        else:
            pass
        e += p
        # print(f"k {k} op {op} override {override} p {p} e {e}", k, op, override, p, e)
    gathered[k] = e
    power[k] = p

z = list(sorted(gathered.items(), key=lambda x: x[1], reverse=True))
print(z)
z = [x[0] for x in z]
print(''.join(z))


ts = [x.strip('\n') for x in open('p3-track.txt').readlines()]
# for e in ts:
#     print(e, len(e))
H = len(ts)
W = len(ts[0])
G = {}
V = {}
for y in range(H):
    for x in range(W):
        G[(x,y)] = ts[y][x]

offsets = [
(1,0), (-1,0), (0,-1),(0,1)
]

done = False
cur = (1,0)
P = ""
while not done:
    done = True
    P += G[cur]
    for o in offsets:
        nxt = (cur[0]+o[0], cur[1]+o[1])
        if nxt in G and G[nxt] != " " and nxt not in V:
            V[cur] = True
            cur = nxt
            done = False
            break

ts = [x for x in P]

from more_itertools import distinct_permutations

xs = [x.strip('\n') for x in open('p3.txt').readlines()]
xs = [x.split(":") for x in xs]
xs = {x[0]: x[1].split(",") for x in xs}
for i,p in enumerate(distinct_permutations(['+', '+', '+', '+', '+', '-', '-', '-', '=', '=', '='])):
    xs[i] = p
print(ts, xs['A'])
print(len(xs), len(ts))
gathered = {k: 0 for k in xs.keys()}
power = {k: 10 for k in xs.keys()}
counts = {}
tracker = {}
ct = 0
for k, v in( xs.items()):
    p = power[k]
    e = gathered[k]
    last_e = e
    last_p = p
    es = []
    pluses = 0
    minuses = 0
    for i in range(2024*len(ts)):
        op = v[i % len(v)]
        override = ts[(i)%len(ts)]
        if override == '+':
            p += 1
            pluses += 1
        elif override == '-':
            p -=1
            minuses += 1
        elif op == '+':
            p += 1
            pluses += 1
        elif op == '-':
            p -= 1
            minuses +=  1
        else:
            pass
        e += p
        if i % 3740 == 0 and (i//3740) > 1:
            j = (i//3740)
            something = e*(j**2) - e
            tracker[k] = something
            if something < 0 or something <= tracker['A']:
                break
            else:
                ct += 1
                break
    counts[k] = {}
    counts[k]['+'] = pluses
    counts[k]['-'] = minuses
    gathered[k] = e
    power[k] = p

print(ct)

