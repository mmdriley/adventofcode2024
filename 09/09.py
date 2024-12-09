from collections import defaultdict

with open('09.txt') as f:
  l = f.read().strip()

diskmap = [int(x) for x in list(l)]

filesmap = diskmap[0::2]
freemap = diskmap[1::2]

print(filesmap)
print(freemap)

# freespace index -> file IDs to include, in order L->R

moves: dict[int, list[int]] = defaultdict(list)

# files that have been moved

moved: set[int] = set()

for currentfile in reversed(range(0, len(filesmap))):
  currentfilelen = filesmap[currentfile]
  for i, v in enumerate(freemap):
    if i >= currentfile:
      break

    if v >= currentfilelen:
      moves[i].append(currentfile)
      freemap[i] -= currentfilelen
      freemap[currentfile-1] += currentfilelen

      moved.add(currentfile)

      break

# now build the disk image

disk: list[int|None] = [0] * filesmap[0]

for i in range(1, len(filesmap)):
  for e in moves[i-1]:
    disk.extend([e] * filesmap[e])
  disk.extend([None] * freemap[i-1])
  if i not in moved:
    disk.extend([i] * filesmap[i])

checksum = 0
for i, v in enumerate(disk):
  if v is not None:
    checksum += i * v

print(checksum)
