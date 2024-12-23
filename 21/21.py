from itertools import pairwise, product
from typing import Iterator, Literal

doorcodes = []
with open('21.txt') as f:
  for l in f:
    doorcodes.append(l.strip())

# (i, j)
# i is distance from top
# j is distance from left

keypad_positions = {
  '7': (0, 0),
  '8': (0, 1),
  '9': (0, 2),
  '4': (1, 0),
  '5': (1, 1),
  '6': (1, 2),
  '1': (2, 0),
  '2': (2, 1),
  '3': (2, 2),
  # GAP: (3, 0)
  '0': (3, 1),
  'A': (3, 2),
}

remote_positions = {
  # GAP: (0, 0)
  '^': (0, 1),
  'A': (0, 2),
  '<': (1, 0),
  'v': (1, 1),
  '>': (1, 2),
}

# assumption: it will never be the right thing to interleave directions
# when we can repeat the same direction
def shortest_paths(startp, endp, gap) -> list[str]:
  (starti, startj) = startp
  (endi, endj) = endp
  
  vpath = ''
  hpath = ''

  i, j = starti, startj
  while i < endi:
    vpath += 'v'
    i += 1
  while i > endi:
    vpath += '^'
    i -= 1
  while j < endj:
    hpath += '>'
    j += 1
  while j > endj:
    hpath += '<'
    j -= 1


  if hpath == '':
    return [vpath]
  elif vpath == '':
    return [hpath]
  elif (starti, endj) == gap:
    return [vpath + hpath]
  elif (endi, startj) == gap:
    return [hpath + vpath]
  else:
    return [vpath + hpath, hpath + vpath]

def keypad_paths_for_doorcode(doorcode) -> Iterator[str]:
  paths = []
  for (k1, k2) in pairwise('A' + doorcode):
    paths.append(shortest_paths(keypad_positions[k1], keypad_positions[k2], (3, 0)))
  for p in product(*paths):
    yield 'A'.join(p) + 'A'


def remote_paths_for_movements(movements) -> Iterator[str]:
  paths = []
  for (b1, b2) in pairwise('A' + movements):
    paths.append(shortest_paths(remote_positions[b1], remote_positions[b2], (0, 0)))
  for p in product(*paths):
    yield 'A'.join(p) + 'A'


def shortest(iter):
  shortest_len = None
  shortest_items = []
  for it in iter:
    if shortest_len is None or len(it) < shortest_len:
      shortest_len = len(it)
      shortest_items = [it]
    elif len(it) == shortest_len:
      shortest_items.append(it)
    # else pass

  return shortest_items


def remote_recurse(movement, depth):
  if depth == 0:
    yield movement
    return

  for m in remote_recurse(movement, depth - 1):
    yield from shortest(remote_paths_for_movements(m))


def physical_keypad_options(doorcode, remote_depth):
  for p1 in keypad_paths_for_doorcode(doorcode):
    for m in remote_recurse(p1, remote_depth):
      yield m


# part 1

complexities = 0
for c in doorcodes:
  n = int(c[:-1])
  p = len(min(physical_keypad_options(c, 2), key=len))
  complexities += n*p

print(complexities)
