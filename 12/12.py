with open('12.txt') as f:
  grid = [list(l.strip()) for l in f]

grid = [['.'] + l + ['.'] for l in grid]
grid = [['.'] * len(grid[0])] + grid + [['.'] * len(grid[0])]


# 90 degree right turns on our i, j grid
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# returns: perimeter, number of sides, set of squares
def fill(istart, jstart) -> tuple[int, int, set[tuple[int, int]]]:
  frontier = [(istart, jstart)]
  explored: set[tuple[int, int]] = set()
  perimeter = 0

  fence_crossings: set[tuple[int, int, int, int]] = set()

  L = grid[istart][jstart]
  assert(L != '.')

  while len(frontier) > 0:
    i, j = frontier.pop()

    if grid[i][j] == '.':
      continue

    if (i, j) in explored:
      continue

    for di, dj in dirs:
      if grid[i + di][j + dj] == L:
        frontier.append((i + di, j + dj))
      else:
        perimeter += 1
        fence_crossings.add((i, j, i + di, j + dj))

    explored.add((i, j))

  sides = 0

  # for every remaining segment of fence, count it as a side and remove
  # all segments that are part of the same side.
  while len(fence_crossings) > 0:
    sides += 1

    i1, j1, i2, j2 = fence_crossings.pop()
    for di, dj in dirs:
      while (i1 + di, j1 + dj, i2 + di, j2 + dj) in fence_crossings:
        i1 += di
        j1 += dj
        i2 += di
        j2 += dj

      while (i1, j1, i2, j2) in fence_crossings:
        fence_crossings.remove((i1, j1, i2, j2))
        i1 -= di
        j1 -= dj
        i2 -= di
        j2 -= dj

  return perimeter, sides, explored


seen: set[tuple[int, int]] = set()
cost1 = cost2 = 0


for i, l in enumerate(grid):
  for j, c in enumerate(l):
    if c == '.':
      continue

    if (i, j) in seen:
      continue

    perimeter, sides, region = fill(i, j)
    seen |= region

    cost1 += len(region) * perimeter
    cost2 += len(region) * sides

# part 1

print(cost1)

# part 2

print(cost2)
