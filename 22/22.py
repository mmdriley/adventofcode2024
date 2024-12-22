from collections import Counter
import more_itertools
from typing import Iterator

initial_secrets = []
with open('22.txt') as f:
  for l in f:
    initial_secrets.append(int(l))


N = 16777216


def secret(n: int) -> int:
  n1 = n * 64
  n = (n ^ n1) % N

  n2 = n // 32
  n = (n ^ n2) % N

  n3 = n * 2048
  n = (n ^ n3) % N

  return n


def secrets(s: int) -> Iterator[int]:
  for _ in range(2000):
    s = secret(s)
    yield s


def prices(s_start: int) -> Iterator[int]:
  yield s_start % 10
  for s in secrets(s_start):
    yield s % 10


# part 1
sum_of_secrets: int = 0
for s in initial_secrets:
  sum_of_secrets += more_itertools.last(secrets(s))

print(sum_of_secrets)


# part 2
alldeltas = Counter()
for s in initial_secrets:
  deltas_seen_here = set()
  for (p1, p2, p3, p4, p5) in more_itertools.sliding_window(prices(s), 5):
    deltas = (p2 - p1, p3 - p2, p4 - p3, p5 - p4)
    if deltas in deltas_seen_here:
      continue
    deltas_seen_here.add(deltas)

    alldeltas.update({deltas: p5})

print(alldeltas.most_common()[:2])
