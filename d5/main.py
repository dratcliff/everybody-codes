xs = [x.strip('\n') for x in open('p3.txt').readlines()]
from collections import defaultdict

class Dance:

    def __init__(self, xs):
        self.xs = [x.split() for x in xs]
        self.xs = [[int(x) for x in y] for y in self.xs]
        self.H = len(self.xs)
        self.W = len(self.xs[0])
        self.xs = [list(row) for row in zip(*self.xs)]        
        self.clapper_col = 0
        self.counts = defaultdict(int)
        self.iterations = 0
        self.biggest = 0
        print(self.H, self.W)

    def a(self):
        self.iterations += 1
        clapper = self.xs[self.clapper_col][0]
        self.xs[self.clapper_col].pop(0)
        side = 0
        self.clapper_col += 1
        self.clapper_col %= self.W
        NH = len(self.xs[self.clapper_col])
        times = clapper / NH
        f_times = clapper // NH
        remainder = times - int(times)
        side = 0
        pos = 0
        if f_times % 2 != 0:
            if remainder == 0:
                side = 0
                pos = NH - 1
            else:
                side = 1
                pos = NH - (clapper % NH) + 1
                
        else:
            if remainder == 0:
                side = 1
                pos = 1
            else:
                side = 0
                pos = (clapper % NH) - 1
       
        
        self.xs[self.clapper_col].insert(pos, clapper)
        num = int(''.join([str(x[0]) for x in self.xs]))
        self.counts[num] += 1
        # if self.counts[num] == 2024:
        #     print(num * self.iterations)
        #     return True
        # else:
        #     return False
        if num > self.biggest:
            self.biggest = num
            print(num)

        return False


d = Dance(xs)

done = False
while not done:
    done = d.a()