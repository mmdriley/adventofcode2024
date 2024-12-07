equations: list[tuple[int, list[int]]] = []

with open('07.txt') as f:
  for l in f:
    (target, operands) = l.strip().split(': ')
    equations.append((int(target), [int(s) for s in operands.split(' ')]))


def evaluate(operands: list[int], opnum: int, n_ops: int) -> int:
  n = operands[0]
  for o in operands[1:]:
    match opnum % n_ops:
      case 0:
        n += o
      case 1:
        n *= o
      case 2:
        n = int(str(n) + str(o))

    opnum //= n_ops

  return n


def total_satisfying(n_ops: int) -> int:
  total = 0

  for (target, operands) in equations:
    opnum = 0
    while opnum < (n_ops ** len(operands)):
      n = evaluate(operands, opnum, n_ops)
      if n == target:
        total += target
        break
      opnum += 1
  
  return total


# part 1

print(total_satisfying(2))

# part 2

print(total_satisfying(3))
