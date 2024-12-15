warehousemap: list[list[str]] = []

roboti = robotj = -1

with open('15.txt') as f:
  for l in f:
    l = l.strip()
    if l == '':
      break

    warehousemap.append(list(l))

    if l.find('@') >= 0:
      roboti = len(warehousemap) - 1
      robotj = l.find('@')

  moves = f.read()

movedirs = {
  '^': (-1, 0),
  '>': (0, 1),
  'v': (1, 0),
  '<': (0, -1),
}

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

gpssum = 0
for i, l in enumerate(warehousemap):
  for j, c in enumerate(l):
    if c == 'O':
      gpssum += i * 100 + j

print(gpssum)
