import networkx as nx

g = nx.Graph()

with open('23.txt') as f:
  for l in f:
    node1, node2 = l.strip().split('-')
    g.add_edge(node1, node2)


# part 1

t_cliques = 0
for c in nx.enumerate_all_cliques(g):
  if len(c) < 3:
    continue
  if len(c) > 3:
    break
  if any([n.startswith('t') for n in c]):
    t_cliques += 1

print(t_cliques)


# part 2

max_c = []
for c in nx.find_cliques(g):
  if len(c) > len(max_c):
    max_c = c

print(','.join(sorted(max_c)))
