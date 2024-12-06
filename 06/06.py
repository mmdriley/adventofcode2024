from collections import defaultdict


with open('06.txt') as f:
  lines = [l.strip() for l in f]

# pad with '%' all around
lines = [f'%{x}%' for x in lines]
dummyline = '%' * len(lines[0])
lines = [dummyline] + lines + [dummyline]

# explode
lines = [list(l) for l in lines]


# find guard
for starti, l in enumerate(lines):
  for startj, c in enumerate(l):
    if c in ['v', '<', '>', '^']:
      break
  else:
    continue

  break


obstacle_positions_creating_cycles: set[tuple[int, int]] = set()


# returns number of positions covered by the walk or
# None if the walk results in a cycle
def walk(i, j, guarddir, nested = False):
  path: dict[tuple[int, int], list[int]] = defaultdict(list)

  # `guarddir` is an index into guardmoves
  # turning 90 degrees right is (dir+1)%4
  guardmoves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

  while True:
    (di, dj) = guardmoves[guarddir]
    nexti, nextj = i + di, j + dj

    match lines[nexti][nextj]:
      case '%':
        return len(path)
      case '.' | '^' as original:
        if not nested and original == '.' and (nexti, nextj) not in path:
          # try putting an obstacle out there first
          lines[nexti][nextj] = '#'
          r = walk(i, j, guarddir, True)
          if r is None:
            obstacle_positions_creating_cycles.add((nexti, nextj))
          lines[nexti][nextj] = '.'

        i, j = nexti, nextj
        if guarddir in path[(i, j)]:
          return None
        path[(i, j)].append(guarddir)
      case '#':
        guarddir = (guarddir + 1) % 4
        path[(i, j)].append(guarddir)
      case _:
        raise ValueError()


# part 1

assert(lines[starti][startj] == '^')
numcovered = walk(starti, startj, 0)
print(numcovered)


# part 2

print(len(obstacle_positions_creating_cycles))
