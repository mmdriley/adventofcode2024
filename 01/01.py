from collections import Counter

a1: list[int] = []
a2: list[int] = []

with open('01.txt') as f:
  for l in f:
    fields = l.split()
    a1.append(int(fields[0]))
    a2.append(int(fields[1]))

a1 = sorted(a1)
a2 = sorted(a2)

# part 1

s = 0

for (x, y) in zip(a1, a2):
  s += abs(x - y)

# part 2

c2 = Counter(a2)

s2 = 0

for n in a1:
  s2 += n * c2[n]

print(s2)
