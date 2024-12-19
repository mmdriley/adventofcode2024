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


def runmap(warehousemap, moves, roboti, robotj):
  warehousemap = copy.deepcopy(warehousemap)

  # print('\n'.join([''.join(l) for l in warehousemap]))

  for m in moves:
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
        assert(nextc == 'O')
        # trying to push one or more boxes
        afteri, afterj = nexti, nextj

        while warehousemap[afteri][afterj] == 'O':
          afteri += movei
          afterj += movej

        if warehousemap[afteri][afterj] == '#':
          continue  # can't push boxes into a wall
        else:
          assert(warehousemap[afteri][afterj] == '.')
          warehousemap[afteri][afterj] = 'O'
          warehousemap[nexti][nextj] = '.'

      # do the move
      assert(warehousemap[nexti][nextj] == '.')
      warehousemap[roboti][robotj] = '.'
      roboti, robotj = nexti, nextj
      warehousemap[roboti][robotj] = '@'

  # print(m)
  # print('\n'.join([''.join(l) for l in warehousemap]))
  return warehousemap


def gpssum(warehousemap):
  gpssum = 0
  for i, l in enumerate(warehousemap):
    for j, c in enumerate(l):
      if c == 'O':
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
