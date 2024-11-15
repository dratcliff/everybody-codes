xs = [x.strip('\n') for x in open('p3.txt').readlines()]
xs = [int(x) for x in xs]

least = 99999999999

for x in xs:
    shortest = x
    ct = 0
    for y in xs:
        ct += abs(shortest-y)
    if ct < least:
        least = ct
print(least)