x = open('p1.txt').readlines()[0]

from collections import Counter
c = Counter(x)

ans = c['B'] + 3*c['C']

print(ans)

x = open('p2.txt').readlines()[0]
x = [x[i:i+2] for i in range(0, len(x), 2)]

S = {
    'x': 0,
    'A': 0,
    'B': 1,
    'C': 3,
    'D': 5
}

ans = 0

for e in x:
    for f in e:
        ans += S[f]
    if 'x' not in e:
        ans += 2

print(ans)


x = open('p3.txt').readlines()[0]
x = [x[i:i+3] for i in range(0, len(x), 3)]

ans = 0

for e in x:
    add = 2 - e.count('x')
    for f in e:
        if f == 'x':
            continue
        ans += S[f] + add

print(ans)