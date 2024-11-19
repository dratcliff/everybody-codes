# blocks = 4098020

# x = 1
# t = 0
# px = 0
# pt = 0
# done = False
# while not done:
#     pt = t
#     t += x
#     px = x
#     x += 2
#     if t > blocks:
#         print(f"{px*(t-blocks)}")
#         done = True


# 0 == center
# 1 == one left
# 2 == two left

# priests = 378
# # priests = 3
# acolytes = 1111
# # acolytes = 5
# blocks = 20240000
# # blocks = 50
# layer = 1
# thickness = 1
# t = []
# t.append(thickness)
# while True:
#     layer += 1
#     thickness = (thickness * priests) % acolytes
#     t.append(0)
#     for i in range(layer):
#         t[i] += thickness
#     total = t[0] + 2*sum(t[1:])
#     if total > blocks:
#         print((total-blocks)*(1+2*len(t[1:])))
#         break


priests = 980692
# priests = 3
acolytes = 10
# acolytes = 5
blocks = 202400000000
blocks = 202400000000
# blocks = 50
layer = 1
thickness = 1
t = []
t.append(thickness)


def can_be_removed(x, layer):
    width = 2*layer-1
    T = 0
    L = layer-1
    for i in range(L):
        T += 2*(((priests % acolytes) * (width % acolytes) * x[i]) % acolytes)

    return T - ((priests % acolytes) * (width % acolytes) * x[0]) % acolytes


while True:
    layer += 1
    thickness = ((thickness % acolytes * priests %
                 acolytes) % acolytes) + acolytes
    t.append(0)
    s = 0
    for i in range(layer):
        t[i] += thickness
        s += 2*t[i]
    total = s - t[0]
    removed = can_be_removed(t, layer)
    if total-removed > blocks:
        print(total-removed-blocks)
        break
