import networkx as nx

bytelist: list[tuple[int, int]] = []

with open('18.txt') as f:
  for l in f:
    x, y = l.strip().split(',')
    bytelist.append((int(x), int(y)))

# start at (0, 0)
# need to reach (70, 70)

# first create the connected graph
g = nx.Graph()

N = 71

for x in range(N):
  for y in range(N):
    for dx, dy in [(0, 1), (1, 0)]:
      (outx, outy) = (x + dx, y + dy)
      if outx < 0 or outy >= N:
        continue
      if outy < 0 or outy >= N:
        continue

      g.add_edge((x, y), (outx, outy))

# part 1

part1g = g.copy()
for x, y in bytelist[:1024]:
  part1g.remove_node((x, y))

print(nx.shortest_path_length(part1g, (0, 0), (N-1, N-1)))

# part 2

i = 0
j = len(bytelist) - 1

# binary search to bisect where we go from passable to impassable
while j - i > 1:
  mid = (i + j) // 2

  part2g = g.copy()
  for x, y in bytelist[:mid+1]:
    part2g.remove_node((x, y))
  
  try:
    nx.shortest_path_length(part2g, (0, 0), (N-1, N-1))
    i = mid
  except nx.NetworkXNoPath:
    j = mid

print(bytelist[j])
