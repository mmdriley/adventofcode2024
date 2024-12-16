from more_itertools import sliding_window

import networkx as nx

mazemap: list[list[str]] = []

starti, startj = -1, -1
endi, endj = -1, -1

with open('16.txt') as f:
  for l in f:
    mazemap.append(list(l.strip()))
    if 'S' in l:
      starti = len(mazemap) - 1
      startj = l.find('S')
    if 'E' in l:
      endi = len(mazemap) - 1
      endj = l.find('E')

# start facing *East*
assert(mazemap[starti][startj] == 'S')
assert(mazemap[endi][endj] == 'E')

movedirs = {
  'E': (0, 1),
  'S': (1, 0),
  'W': (0, -1),
  'N': (-1, 0),
}

turns = ['NE', 'SE', 'SW', 'NW']

g = nx.MultiGraph()

# add edges for:
#   this square to next square by compass direction
#   rotations within this square
for i, l in enumerate(mazemap):
  for j, _ in enumerate(l):
    for movedir, (di, dj) in movedirs.items():
      g.add_edge((i, j, movedir), (i + di, j + dj, movedir), cost=1)
    for turn in turns:
      g.add_edge((i, j, turn[0]), (i, j, turn[1]), cost=1000)

# remove edges for walls
for i, l in enumerate(mazemap):
  for j, c in enumerate(l):
    if c != '#':
      continue
    for movedir in movedirs:
      g.remove_node((i, j, movedir))

# avoid needing to search for end position in all directions
for turn in turns:
  g.add_edge((endi, endj, turn[0]), (endi, endj, turn[1]), cost=0.001)

# part 1

mincost = nx.shortest_path_length(g, (starti, startj, 'E'), (endi, endj, 'E'), weight='cost')
print(mincost)

# part 2

distances1, _ = nx.single_source_dijkstra(g, (starti, startj, 'E'), weight='cost')
distances2, _ = nx.single_source_dijkstra(g, (endi, endj, 'E'), weight='cost')

onbest = set()

# squares on the "best" path have costs from source+dest that add to precisely mincost
for i in range(len(mazemap)):
  for j in range(len(mazemap[0])):
    for dir in movedirs:
      n = (i, j, dir)
      if n not in distances1 or n not in distances2:
        continue
      cost = distances1[n] + distances2[n]
      if cost == mincost:
        onbest.add((i, j))

print(len(onbest))
