from collections import defaultdict
import itertools
from math import gcd

freqpositions: dict[str, list[tuple[int, int]]] = defaultdict(list)
W = H = 0


with open('08.txt') as f:
  for i, l in enumerate(f):
    H = i
    for j, c in enumerate(l.strip()):
      W = j
      if c == '.':
        continue
      freqpositions[c].append((i, j))


def inbounds(t):
  i, j = t

  if i < 0 or i > H:
    return False
  if j < 0 or j > W:
    return False

  return True


antinodes1 = set()
antinodes2 = set()


for _, v in freqpositions.items():
  for (i1, j1), (i2, j2) in itertools.combinations(v, 2):
    # the slope from a1 to a2
    si, sj = i2 - i1, j2 - j1

    n = (i1 + 2*si, j1 + 2*sj)
    if inbounds(n):
      antinodes1.add(n)

    n = (i2 - 2*si, j2 - 2*sj)
    if inbounds(n):
      antinodes1.add(n)

    # This wasn't necessary for my input, but it does seem like in part 2
    # we could have antennas at (4, 4) and (6, 6) and need to recognize
    # that (5, 5) is an antinode since it's a colinear grid point.
    #
    # d = gcd(si, sj)
    # si //= d
    # sj //= d

    p = (i1, j1)
    while inbounds(p):
      antinodes2.add(p)
      pi, pj = p
      p = (pi - si, pj - sj)

    p = (i1, j1)
    while inbounds(p):
      antinodes2.add(p)
      pi, pj = p
      p = (pi + si, pj + sj)


# part 1
print(len(antinodes1))

# part 2

print(len(antinodes2))
