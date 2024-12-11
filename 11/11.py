from functools import cache

with open('11.txt') as f:
  stones = [int(x) for x in f.read().strip().split()]

@cache
def blinklen(n: int, remaining: int) -> int:
  if remaining == 0:
    return 1

  if n == 0:
    return blinklen(1, remaining - 1)
  
  sn = str(n)
  if len(sn) % 2 == 0:
    sn1 = sn[:len(sn)//2]
    sn2 = sn[len(sn)//2:]
    return blinklen(int(sn1), remaining - 1) + blinklen(int(sn2), remaining - 1)

  return blinklen(2024 * n, remaining - 1)

# part 1

print(sum([blinklen(n, 25) for n in stones]))

# part 2

print(sum([blinklen(n, 75) for n in stones]))
