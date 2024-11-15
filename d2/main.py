xs = [x.strip('\n') for x in open('p1.txt').readlines()]
words = xs[0].split(':')[1].split(',')
sentence = xs[2].split()
rw = 0

for s in sentence:
    for w in words:
        if w in s:
            rw += 1

print(rw)

rw = 0
xs = [x.strip('\n') for x in open('p2.txt').readlines()]
words = xs[0].split(':')[1].split(',')
sentences = [x.split() for x in xs[2:]]
for sentence in sentences:
    for s in sentence:
        found = [False]*len(s)
        for i in range(len(s)):
            for w in words:
                if len(w) > len(s) + i:
                    continue
                subword = s[i:i+len(w)]
                if subword == w or "".join(reversed(subword)) == w:
                    for j in range(i, i+len(w)):
                        found[j] = True
        rw += sum([1 for x in found if x])

print(rw)


rw = 0
xs = [x.strip('\n') for x in open('p3.txt').readlines()]
words = xs[0].split(':')[1].split(',')
sentences = [x for x in xs[2:]]
print(words, sentences)
height = len(sentences)
width = len(sentences[0])
grid = {(x,y): sentences[y][x] for x in range(width) for y in range(height)}
found = {(x,y): False for x in range(width) for y in range(height)}
for y in range(height):
    for x in range(width):
        for w in words:
            word_length = len(w)
            # up
            if y - word_length < -1:
                pass
            else:
                maybe = "".join([grid[(x,(y-i))] for i in range(word_length)])
                if maybe in words or "".join(reversed(maybe)) in words:
                    # print("up", maybe)
                    for i in range(word_length):
                        found[(x,(y-i))] = True
            # down
            if y + word_length > height:
                pass
            else:
                maybe = "".join([grid[(x,(y+i))] for i in range(word_length)])
                if maybe in words or "".join(reversed(maybe)) in words:
                    # print("down", maybe)
                    for i in range(word_length):
                        found[(x,(y+i))] = True
            # left
            maybe = "".join([grid[((x-i)%width,y)] for i in range(word_length)])
            if maybe in words or "".join(reversed(maybe)) in words:
                # print("left", maybe)
                for i in range(word_length):
                    found[((x-i)%width,y)] = True
            # right
            maybe = "".join([grid[((x+i)%width,y)] for i in range(word_length)])
            if maybe in words or "".join(reversed(maybe)) in words:
                # print("right", maybe)
                for i in range(word_length):
                    found[((x+i)%width,y)] = True
print(sum([1 for x in found.values() if x]))