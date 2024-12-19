import re2 as re

designs = []

with open('19.txt') as f:
  patterns = f.readline().strip().split(', ')
  f.readline()
  for l in f:
    designs.append(l.strip())

possiblere = re.compile('^(' + '|'.join(patterns) + ')*$')

print(sum([1 if possiblere.match(d) else 0 for d in designs]))
