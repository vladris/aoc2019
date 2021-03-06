p1, p2 = open("input").read().split("\n\n")

p1 = list(map(int, p1.strip().split("\n")[1:]))
p2 = list(map(int, p2.strip().split("\n")[1:]))

import random

def combat(p1, p2):
    prev1, prev2 = set(), set()
    while p1 and p2:
        h1, h2 = str(p1), str(p2)

        if h1 in prev1 or h2 in prev2:
            return p1, 0

        prev1.add(h1)
        prev2.add(h2)

        c1, c2 = p1.pop(0), p2.pop(0)

        if len(p1) >= c1 and len(p2) >= c2:
            _, i = combat(p1[:c1], p2[:c2])
            if i == 0:
                p1 += [c1, c2]
            else:
                p2 += [c2, c1]
        elif c1 > c2:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]

    return (p1, 0) if p1 else (p2, 1)

p, _ = combat(p1, p2)

total = 0
for i, c in enumerate(reversed(p)):
    total += (i + 1) * c

print(total)
