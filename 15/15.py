import copy

originalmap: list[list[str]] = []

roboti_start = robotj_start = -1

with open('15.txt') as f:
  for l in f:
    l = l.strip()
    if l == '':
      break

    originalmap.append(list(l))

    if l.find('@') >= 0:
      roboti_start = len(originalmap) - 1
      robotj_start = l.find('@')

  moves = f.read()

movedirs = {
  '^': (-1, 0),
  '>': (0, 1),
  'v': (1, 0),
  '<': (0, -1),
}

# (i, j) is a part of a box to be pushed by (di, dj)
def pushbox(m: list[list[str]], boxi: int, boxj: int, di: int, dj: int) -> bool:
  match m[boxi][boxj]:
    case 'O':
      old_coords = [(boxi, boxj)]
    case '[':
      assert(m[boxi][boxj+1] == ']')
      old_coords = [(boxi, boxj), (boxi, boxj+1)]
    case ']':
      assert(m[boxi][boxj-1] == '[')
      old_coords = [(boxi, boxj-1), (boxi, boxj)]
    case _:
      raise ValueError()  # not a box

  # make room for this box
  for oldi, oldj in old_coords:
    newi = oldi + di
    newj = oldj + dj

    match m[newi][newj]:
      case '.':
        pass  # nothing to do
      case '[' if dj == -1:
        assert(m[oldi][oldj] == ']')
      case ']' if dj == 1:
        assert(m[oldi][oldj] == '[')
      case '#':
        return False  # hit a wall, return failure
      case '[' | ']' | 'O' as boxchar:
        # We ignored the cases where boxes were pushing into themselves, so
        # this is pushing into a new box. Try pushing it.
        if not pushbox(m, newi, newj, di, dj):
          return False
        assert(m[newi][newj] == '.')

  # take care to capture the old chars, erase the old coords,
  # then write the new ones, to avoid ever reading our own writes
  # within a loop
  old_chars = [m[oldi][oldj] for (oldi, oldj) in old_coords]

  for (oldi, oldj) in old_coords:
    m[oldi][oldj] = '.'

  for ((oldi, oldj), c) in zip(old_coords, old_chars):
    newi = oldi + di
    newj = oldj + dj

    m[newi][newj] = c

  return True


def runmap(warehousemap, moves, roboti, robotj):
  warehousemap = copy.deepcopy(warehousemap)

  # print('\n'.join([''.join(l) for l in warehousemap]))

  for m in moves:
    # print(m)
    assert(warehousemap[roboti][robotj] == '@')
    if m == '\n':
      continue

    assert(m in movedirs)

    movei, movej = movedirs[m]
    nexti, nextj = roboti + movei, robotj + movej

    nextc = warehousemap[nexti][nextj]

    if nextc == '#':
      pass
    else:
      # going to move
      if nextc == '.':
        pass
      else:
        assert(nextc in ['[', ']', 'O'])
        mapafter = copy.deepcopy(warehousemap)
        if pushbox(mapafter, nexti, nextj, movei, movej):
          warehousemap = mapafter
        else:
          continue  # can't push box

      # do the move
      assert(warehousemap[nexti][nextj] == '.')
      warehousemap[roboti][robotj] = '.'
      roboti, robotj = nexti, nextj
      warehousemap[roboti][robotj] = '@'

    # print('\n'.join([''.join(l) for l in warehousemap]))
  return warehousemap


def gpssum(warehousemap):
  gpssum = 0
  for i, l in enumerate(warehousemap):
    for j, c in enumerate(l):
      if c in ['O', '[']:
        gpssum += i * 100 + j

  return gpssum


# part 1

part1map = runmap(originalmap, moves, roboti_start, robotj_start)
print(gpssum(part1map))

# part 2

part2map = copy.deepcopy(originalmap)

replacements = {
  '#': '##',
  '.': '..',
  '@': '@.',
  'O': '[]',
}

for i in range(len(part2map)):
  part2map[i] = sum([list(replacements[x]) for x in part2map[i]], [])

# print('\n'.join([''.join(l) for l in warehousemap]))

roboti, robotj = roboti_start, robotj_start * 2
assert(part2map[roboti][robotj] == '@')

part2map = runmap(part2map, moves, roboti, robotj)
print(gpssum(part2map))
