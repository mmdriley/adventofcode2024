# keys start with ..... and end with #####
# locks start with ##### and end with .....
# everything is 7 rows tall

Tumblers = list[int]
keys: list[Tumblers] = []
locks: list[Tumblers] = []


def additem(item: list[Tumblers]):
  if item[0] == '.....':
    assert(item[6] == '#####')
    dest = keys
  elif item[0] == '#####':
    assert(item[6] == '.....')
    dest = locks
  else:
    raise ValueError

  item = item[1:-1]
  tumblers = [0, 0, 0, 0, 0]
  for i in range(5):
    tumblers[i] = sum([x[i] == '#' for x in item])
  dest.append(tumblers)


with open('25.txt') as f:
  thisitem = []
  for l in f:
    l = l.strip()
    if l != '':
      thisitem.append(l)
      continue
    else:
      assert(len(thisitem) == 7)
      additem(thisitem)
      thisitem = []

  additem(thisitem)


# part 1

viable_pairs = []

for k in keys:
  for l in locks:
    for i in range(5):
      if k[i] + l[i] > 5:
        break
    else:
      viable_pairs.append((k, l))

print(len(viable_pairs))
