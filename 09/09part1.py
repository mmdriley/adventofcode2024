with open('09.txt') as f:
  l = f.read().strip()

diskmap = [int(x) for x in list(l)]

disk: list[int|None] = [0] * diskmap[0]

id = 1
mapindex = 1

while mapindex < len(diskmap):
  freesize, filesize = diskmap[mapindex:mapindex+2]
  mapindex += 2

  disk += [None] * freesize
  disk += [id] * filesize
  id += 1

lastused = len(disk) - 1
firstfree = disk.index(None)

while True:
  disk[firstfree] = disk[lastused]
  disk[lastused] = None

  firstfree = disk.index(None, firstfree)
  while disk[lastused] == None:
    lastused -= 1
    if lastused < firstfree:
      break
  else:
    continue

  break

checksum = 0
for i, v in enumerate(disk):
  if v is not None:
    checksum += i * v

print(checksum)
