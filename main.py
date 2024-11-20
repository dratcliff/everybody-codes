OFFSETS = [(1,0), (-1,0), (0,-1), (0,1)]
OFFSETS_D = [(1,0), (-1,0), (0,-1), (0,1), (1,1), (1,-1), (-1,1), (-1,-1)]

def to_grid(xs):
    H = len(xs)
    W = len(xs[0])
    G = {}
    for y in range(H):
        for x in range(W):
            G[(x,y)] = xs[y][x]

    return (G, W, H)

def get_lines(filename):
    return [x.strip('\n') for x in open(filename).readlines()]

xs = get_lines('p1-test.txt')
print(xs)