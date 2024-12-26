from functools import cache
from itertools import pairwise

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

@cache
def all_moves(pos1, pos2, gap) -> list[str]:
  if pos1 == gap:
    return []

  if pos1 == pos2:
    return ['']

  (i1, j1) = pos1
  (i2, j2) = pos2

  moves = []

  if i1 < i2:
    moves += ['v' + x for x in all_moves((i1 + 1, j1), pos2, gap)]
  if i1 > i2:
    moves += ['^' + x for x in all_moves((i1 - 1, j1), pos2, gap)]
  if j1 < j2:
    moves += ['>' + x for x in all_moves((i1, j1 + 1), pos2, gap)]
  if j1 > j2:
    moves += ['<' + x for x in all_moves((i1, j1 - 1), pos2, gap)]
  
  return moves


def all_keypad_moves(c1: str, c2: str) -> list[str]:
  return all_moves(keypad_positions[c1], keypad_positions[c2], (3, 0))


def all_remote_moves(c1: str, c2: str) -> list[str]:
  return all_moves(remote_positions[c1], remote_positions[c2], (0, 0))


# lowest cost way to push c2 after c1 at moveL, evaluated at maxL
# assume everything > moveL starts at 'A'
@cache
def push_cost(c1, c2, pushL, maxL) -> int:
  if pushL >= maxL:
    return 1  # just push it

  # push c2 after c1 at pushL means pushing remote buttons at pushL + 1
  if pushL == 0:
    potential_moves = all_keypad_moves(c1, c2)
  else:
    potential_moves = all_remote_moves(c1, c2)

  # at level pushL + 1, this means pushing these buttons then moving to 'A' and pressing it
  costs = []
  for m in potential_moves:
    cost = 0
    for (movec1, movec2) in pairwise('A' + m + 'A'):
      cost += push_cost(movec1, movec2, pushL + 1, maxL)
    costs.append(cost)
  
  return min(costs)


def doorcode_cost(doorcode: str, n_remotes: int) -> int:
  cost = 0
  for (c1, c2) in pairwise('A' + doorcode):
    cost += push_cost(c1, c2, 0, n_remotes)
  return cost


# part 1

complexity = 0
for c in doorcodes:
  n = int(c[:-1])
  complexity += n * doorcode_cost(c, 3)

print(complexity)


# part 2

complexity = 0
for c in doorcodes:
  n = int(c[:-1])
  complexity += n * doorcode_cost(c, 26)

print(complexity)
