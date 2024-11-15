xs = [x.strip('\n') for x in open('p2.txt').readlines()]
H = len(xs)
W = len(xs[0])
G = {(x,y): xs[y][x] for x in range(W) for y in range(H)}
for x in range(W):
    for y in range(H):
        if G[(x,y)] == '#':
            G[(x,y)] = 1
        else:
            G[(x,y)] = 0

OFFSETS = [(1,0), (-1,0), (0,-1), (0,1)]

done = False
while not done:
    NG = {}
    done = True
    for x in range(W):
        for y in range(H):
            dug = True
            pt = (x,y)
            NG[(x,y)] = G[pt]
            if G[pt] > 0:
                for o in OFFSETS:
                    nxt = (x+o[0],y+o[1])
                    if nxt in G:
                        if G[nxt] != G[pt]:
                            dug = False
                            break
            else:
                dug = False
            if dug:
                NG[pt] += 1
                done = False
    G = NG

print(sum(G.values()))


xs = [x.strip('\n') for x in open('p3.txt').readlines()]
H = len(xs)
W = len(xs[0])
G = {(x,y): xs[y][x] for x in range(W) for y in range(H)}
for x in range(W):
    for y in range(H):
        if G[(x,y)] == '#':
            G[(x,y)] = 1
        else:
            G[(x,y)] = 0

OFFSETS = [(1,0), (-1,0), (0,-1), (0,1), (1,1),(1,-1),(-1,1),(-1,-1)]

done = False
while not done:
    NG = {}
    done = True
    for x in range(W):
        for y in range(H):
            dug = True
            pt = (x,y)
            NG[(x,y)] = G[pt]
            if G[pt] > 0:
                for o in OFFSETS:
                    nxt = (x+o[0],y+o[1])
                    G_nxt = G[nxt] if nxt in G else 0
                    if G_nxt != G[pt]:
                        dug = False
                        break
            else:
                dug = False
            if dug:
                NG[pt] += 1
                done = False
    G = NG


print(sum(G.values()))