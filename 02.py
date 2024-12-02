def is_safe(r: list[int]):
  deltas = [nextval - prevval
            for (nextval, prevval) in zip(r[1:], r[:-1])]

  if all([1 <= n <= 3 for n in deltas]):
    return True
  
  if all([-3 <= n <= -1 for n in deltas]):
    return True

  return False


def is_safe_after_problem_dampener(r: list[int]):
  for i in range(len(r)):
    if is_safe(r[:i] + r[i+1:]):
      return True

  return False


c1 = 0
c2 = 0
with open('inputs/02.txt') as f:
  for l in f:
    report = [int(x) for x in l.split()]
    if is_safe(report):
      c1 += 1
    if is_safe_after_problem_dampener(report):
      c2 += 1

# part 1
print(c1)

# part 2
print(c2)
