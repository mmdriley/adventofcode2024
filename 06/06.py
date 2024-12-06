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


def walk():
  path: set[tuple[int, int, int]] = set()

  def covered():
    return set([(i, j) for (i, j, _) in path])

  i, j = starti, startj
  assert(lines[i][j] == '^')

  # `guarddir` is an index into guardmoves
  # turning 90 degrees right is (dir+1)%4
  guardmoves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  guarddir = 0

  while True:
    (di, dj) = guardmoves[guarddir]
    nexti, nextj = i + di, j + dj

    match lines[nexti][nextj]:
      case '%':
        return covered(), False
      case 'X' | '.' | '^':
        i, j = nexti, nextj
        if (i, j, guarddir) in path:
          return covered(), True
        path.add((i, j, guarddir))
      case '#' | 'O':
        guarddir = (guarddir + 1) % 4
        path.add((i, j, guarddir))
      case _:
        print(lines[nexti][nextj])
        raise ValueError()


# part 1

covered_unblocked, is_cycle = walk()
assert(not is_cycle)
print(len(covered_unblocked))


# part 2

cycles = 0
for (i, j) in covered_unblocked:
  if lines[i][j] != '.':
    continue

  lines[i][j] = 'O'
  _, is_cycle = walk()
  if is_cycle:
    cycles += 1
  lines[i][j] = '.'

print(cycles)
