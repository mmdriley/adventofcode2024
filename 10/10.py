with open('10.txt') as f:
  trailmap = f.read().split('\n')

trailmap = [[100] + [int(x) for x in list(l)] + [100] for l in trailmap]
trailmap = [[100] * len(trailmap[0])] + trailmap + [[100] * len(trailmap[0])]


# if `reached` is non-None, coordinates for every `9` reached are added
# to it and new paths ending at that `9` won't be tallied.
def trailsfrom(i: int, j: int, reached: set[tuple[int, int]] | None) -> int:
  start = trailmap[i][j]

  if start == 9:
    if reached is None:
      return 1

    if (i, j) in reached:
      return 0

    reached.add((i, j))
    return 1

  trails = 0

  for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    if trailmap[i + di][j + dj] == start + 1:
      trails += trailsfrom(i + di, j + dj, reached)

  return trails


total1 = 0
total2 = 0


for i, l in enumerate(trailmap):
  for j, height in enumerate(l):
    if height != 0:
      continue

    total1 += trailsfrom(i, j, set())
    total2 += trailsfrom(i, j, None)


# part 1
print(total1)

# part 2
print(total2)
