equations: list[tuple[int, list[int]]] = []

with open('07.txt') as f:
  for l in f:
    (target, operands) = l.strip().split(': ')
    equations.append((int(target), [int(s) for s in operands.split(' ')]))


def can_satisfy(target: int, operands: list[int], use_concat: bool) -> bool:
  match operands:
    case [n]:
      return n == target
    case [a, b, *rest]:
      if can_satisfy(target, [a+b, *rest], use_concat):
        return True
      if can_satisfy(target, [a*b, *rest], use_concat):
        return True
      if (use_concat
          and can_satisfy(target, [int(str(a)+str(b)), *rest], use_concat)):
        return True

  return False


total1 = 0
total2exclusive = 0

for (target, operands) in equations:
  if can_satisfy(target, operands, False):
    total1 += target
  elif can_satisfy(target, operands, True):
    total2exclusive += target


# part 1

print(total1)

# part 2

print(total1 + total2exclusive)
