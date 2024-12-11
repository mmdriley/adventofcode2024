from typing import Iterable

with open('11.txt') as f:
  stones = [int(x) for x in f.read().strip().split()]

def blink(n: int) -> list[int]:
  if n == 0:
    return [1]
  
  sn = str(n)
  if len(sn) % 2 == 0:
    return [int(sn[:len(sn)//2]), int(sn[len(sn)//2:])]

  return [n * 2024]

def flatten(ll: list[list[int]]) -> Iterable[int]:
  for l in ll:
    for x in l:
      yield x

for i in range(75):
  print(i)
  stones = list(flatten([blink(n) for n in stones]))

print(len(stones))
