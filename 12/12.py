with open('12.txt') as f:
  grid = [list(l.strip()) for l in f]

grid = [['.'] + l + ['.'] for l in grid]
grid = [['.'] * len(grid[0])] + grid + [['.'] * len(grid[0])]


# 90 degree right turns on our i, j grid
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# returns: perimeter, sides, set of squares
def fill(istart, jstart) -> tuple[int, set[tuple[int, int]]]:
  frontier = [(istart, jstart)]
  explored: set[tuple[int, int]] = set()
  perimeter = 0

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

    explored.add((i, j))

  return perimeter, explored



seen: set[tuple[int, int]] = set()
total_fence_cost = 0


for i, l in enumerate(grid):
  for j, c in enumerate(l):
    if c == '.':
      continue

    if (i, j) in seen:
      continue

    perimeter, region = fill(i, j)
    seen |= region

    total_fence_cost += len(region) * perimeter

print(total_fence_cost)
