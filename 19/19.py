from functools import cache
import re2 as re

designs = []

with open('19.txt') as f:
  patterns = f.readline().strip().split(', ')
  f.readline()
  for l in f:
    designs.append(l.strip())


@cache
def ways_to_make(design: str):
  if design == '':
    return 1

  s = 0
  for p in patterns:
    if design.startswith(p):
      s += ways_to_make(design[len(p):])

  return s


# part 1

possible = 0

for d in designs:
  if ways_to_make(d) > 0:
    possible += 1

print(possible)

# part 2

ways = 0

for d in designs:
  ways += ways_to_make(d)

print(ways)
