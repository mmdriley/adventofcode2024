import networkx as nx

mazemap: list[list[str]] = []

starti, startj = -1, -1
endi, endj = -1, -1

with open('21.txt') as f:
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


def timesaved(startn: Pos, endn: Pos) -> int:
  if startn not in path_with_pos or endn not in path_with_pos:
    return 0
  
  return abs(path_with_pos[endn] - path_with_pos[startn])


# part 1

over100: int = 0
for i, l in enumerate(mazemap):
  for j, c in enumerate(l):
    if c != '#':
      continue

    saved_v = timesaved((i + 1, j), (i - 1, j))
    if saved_v > 100:
      over100 += 1
    saved_h = timesaved((i, j - 1), (i, j + 1))
    if saved_h > 100:
      over100 += 1

print(over100)
