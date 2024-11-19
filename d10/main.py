xs = [x.strip('\n') for x in open('p2.txt').readlines()]

H = len(xs)
W = len(xs[0])

G = {}

for y in range(H):
    for x in range(W):
        print(y,x)
        G[(x,y)] = xs[y][x]

c = 0
S = 0
for i in range(15):
    for j in range(7):
        
        letters_x = {}
        letters_y = {}

        for y in range(8):
            oy = y
            letters = []
            y = (y+j*9)
            for x in range(8):
                x = (x+i*9)
                print(i,j, x, y)
                letter = G[(x,y)]
                if letter not in ("*", "."):
                    letters.append(letter)
            letters_y[oy] = set(tuple(letters))

        for x in range(8):
            ox = x
            x = (x+i*9)
            letters = []
            for y in range(8):
                y = (y+j*9)
                letter = G[(x,y)]
                if letter not in ("*", "."):
                    letters.append(letter)
            letters_x[ox] = set(tuple(letters))

        s = ""
        for y in range(2, 6):
            for x in range(2, 6):
                s += list(letters_x[x] & letters_y[y])[0]

        print(s)

        t = 0
        for k in range(len(s)):
            t += (k+1)*(ord(s[k])-64)

        S += t
        c += 1

        print(c, S)