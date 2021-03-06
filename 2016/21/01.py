import re

input = open("input").readlines()

scramble = list("abcdefgh")

for line in input:
    m = re.match(r"swap position (\d+) with position (\d+)", line)
    if m:
        m1, m2 = int(m[1]), int(m[2])
        scramble[m1], scramble[m2] = scramble[m2], scramble[m1]

    m = re.match(r"swap letter (\w) with letter (\w)", line)
    if m:
        l1, l2 = m[1], m[2]
        scramble = [l2 if c == l1 else l1 if c == l2 else c for c in scramble]

    m = re.match(r"rotate left (\d+)", line)
    if m:
        r = int(m[1])
        scramble = scramble[r:] + scramble[:r]

    m = re.match(r"rotate right (\d+)", line)
    if m:
        r = -int(m[1]) % len(scramble)
        scramble = scramble[r:] + scramble[:r]

    m = re.match(r"rotate based on position of letter (\w)", line)
    if m:
        r = scramble.index(m[1])
        r += 2 if r >= 4 else 1
        r = -r % len(scramble)
        scramble = scramble[r:] + scramble[:r]

    m = re.match(r"reverse positions (\d+) through (\d+)", line)
    if m:
        m1, m2 = int(m[1]), int(m[2])
        while m1 < m2:
            scramble[m1], scramble[m2] = scramble[m2], scramble[m1]
            m1 += 1
            m2 -= 1

    m = re.match(r"move position (\d+) to position (\d+)", line)
    if m:
        m1, m2 = int(m[1]), int(m[2])
        l = scramble.pop(m1)
        scramble.insert(m2, l)

print("".join(scramble))
