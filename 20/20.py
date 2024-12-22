import networkx as nx

mazemap: list[list[str]] = []

starti, startj = -1, -1
endi, endj = -1, -1

with open('20.txt') as f:
  for l in f:
    mazemap.append(list(l.strip()))
    if 'S' in l:
      starti = len(mazemap) - 1
      startj = l.find('S')
    if 'E' in l:
      endi = len(mazemap) - 1
      endj = l.find('E')

assert(mazemap[starti][startj] == 'S')
assert(mazemap[endi][endj] == 'E')

g = nx.Graph()

for i, l in enumerate(mazemap):
  for j, c in enumerate(l):
    if c == '#':
      if g.has_node((i, j)):
        g.remove_node((i, j))
    else:
      g.add_edge((i, j), (i+1, j))
      g.add_edge((i, j), (i, j+1))

path = nx.shortest_path(g, (starti, startj), (endi, endj))

Pos = tuple[int, int]
path_with_pos: dict[Pos, int] = dict()

for i, n in enumerate(path):
  path_with_pos[n] = i


def distance(startn: Pos, endn: Pos) -> int:
  (i1, j1) = startn
  (i2, j2) = endn

  return abs(i2 - i1) + abs(j2 - j1)


Cheat = tuple[Pos, Pos]
def ncheats(maxdist: int, minsaving: int) -> int:
  n = 0
  for begin in range(len(path)):
    for end in range(begin + minsaving, len(path)):
      d = distance(path[begin], path[end])
      if d > maxdist:
        continue
      saving = (end - begin) - d
      if saving >= minsaving:
        n += 1
  return n


# part 1

print(ncheats(2, 100))

# part 2

print(ncheats(20, 100))
