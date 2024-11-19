xs = [x.strip('\n') for x in open('p3.txt').readlines()]

H = len(xs)
W = len(xs[0])
row_ct = (H-2)//6
col_ct = (W-2)//6
G = {}

for y in range(H):
    for x in range(W):
        G[(x,y)] = xs[y][x]

def p():
    s = ""
    for y in range(H):
        for x in range(W):
            s += G[(x,y)]
        s += "\n"
    print(s)


def p2(x_i, y_i):
    modified = False
    letters_x = {}
    letters_x_cts = {}
    letters_y = {}
    letters_y_cts = {}
    x_start = x_i*6
    x_end = x_start+8
    y_start = y_i*6
    y_end = y_start+8

    s = ""
    for y in range(y_start+2, y_end-2):
        for x in range(x_start+2, x_end-2):
            s += G[(x,y)]
    if "." in s or "?" in s:
        return 0

    t = 0
    for k in range(len(s)):
        t += (k+1)*(ord(s[k])-64)

    return t

from collections import defaultdict

def solve(x_i, y_i):
    H = {}
    modified = False
    letters_x = {}
    letters_x_cts = {}
    letters_y = {}
    letters_y_cts = {}
    x_start = x_i*6
    x_end = x_start+8
    y_start = y_i*6
    y_end = y_start+8
    runic_letters = set()

    for y in range(y_start, y_end):
        letters = []
        letters_y_cts[y] = defaultdict(int)
        for x in range(x_start, x_end):
            letter = G[(x,y)]
            # if letter not in ("*", ".", "?"):
            letters.append(letter)
            letters_y_cts[y][letter] += 1
            if (y_start+2 >= y >= y_end-2) and (x_start+2 >= x >= x_end-2):
                runic_letters.add(letter)
        letters_y[y] = set(tuple(letters))

    for x in range(x_start, x_end):
        letters = []
        letters_x_cts[x] = defaultdict(int)
        for y in range(y_start, y_end):
            letter = G[(x,y)]
            # if letter not in ("*", ".", "?"):
            letters.append(letter)
            letters_x_cts[x][letter] += 1
        letters_x[x] = set(tuple(letters))

    s = ""
    for y in range(y_start+2, y_end-2):
        for x in range(x_start+2, x_end-2):
            found_x=[k for k, v in letters_x_cts[x].items() if v >= 1 and k not in ("*", ".", "?") and k not in runic_letters]
            found_y=[k for k, v in letters_y_cts[y].items() if v >= 1 and k not in ("*", ".", "?") and k not in runic_letters]
            found=list(set(tuple(found_x)) & set(tuple(found_y)))
            if len(found) == 1 and G[(x,y)] in (".", "?"):
                G[(x,y)] = found[0]
                runic_letters.add(found[0])
                letters_x_cts[x][found[0]] += 1
                letters_y_cts[y][found[0]] += 1
                modified = True

    for y in range(y_start, y_end):
        letters = []
        for x in range(x_start, x_end):
            letter = G[(x,y)]
            if letter in ("?", "."):
                missing_x=[k for k, v in letters_x_cts[x].items() if v == 1 and k not in ("*", ".", "?")]
                missing_y=[k for k, v in letters_y_cts[y].items() if v == 1 and k not in ("*", ".", "?")]
                empty_in_col = sum([v for k, v in letters_y_cts[y].items() if k in ("*", ".", "?")])
                empty_in_row = sum([v for k, v in letters_x_cts[x].items() if k in ("*", ".", "?")])
                missing = list(set(missing_x) ^ set(missing_y))
                if len(missing_x) == 1 and missing_x[0] in missing and empty_in_row == 1:
                    missing = missing_x
                elif len(missing_y) == 1 and missing_y[0] in missing and empty_in_col == 1:
                    missing = missing_y
                if len(missing) == 1 and G[(x,y)] in (".", "?") and (empty_in_col == 1 or empty_in_row == 1):
                    if (y_start+2 >= y >= y_end-2) and (x_start+2 >= x >= x_end-2) and missing[0] in runic_letters:
                        continue
                    G[(x,y)] = missing[0]
                    letters_x_cts[x][missing[0]] += 1
                    letters_y_cts[y][missing[0]] += 1
                    if (y_start+2 >= y >= y_end-2) and (x_start+2 >= x >= x_end-2):
                        runic_letters.add(missing[0])
                    modified = True


    # for k, v in H.items():
    #     G[k] = v

    return modified

done = False
while not done:
    done = True
    for y in range(row_ct):
        for x in range(col_ct):
            yo = not solve(x,y)
            done = yo and done

t = 0
for y in range(row_ct):
        for x in range(col_ct):
            t += p2(x,y)
print(t)