from functools import cache

startwires: dict[str, int] = {}

Gate = tuple[str, str, str]  # w1, op, w2

# w3 = Gate
gates: dict[str, Gate] = {}

with open('24.txt') as f:
  for l in f:
    l = l.strip()
    if l == '':
      break
    wirename, wireval = l.split(': ')
    startwires[wirename] = int(wireval)

  for l in f:
    l = l.strip()
    w1, op, w2, arrow, w3 = l.split(' ')
    assert(arrow == '->')
    gates[w3] = (w1, op, w2)
  

@cache
def evalwire(wire: str) -> int | None:
  if wire in startwires:
    return startwires[wire]
  
  if wire in gates:
    (w1, op, w2) = gates[wire]
    w1val = evalwire(w1)
    w2val = evalwire(w2)
    assert(w1val is not None and w2val is not None)
    match op:
      case 'AND':
        output = w1val & w2val
      case 'OR':
        output = w1val | w2val
      case 'XOR':
        output = w1val ^ w2val
      case _:
        raise ValueError
    return output

  return None


zwire = 0
addbit = 1
result = 0

while True:
  zbit = evalwire('z' + str(zwire).rjust(2, '0'))
  if zbit is None:
    break
  result = result | (addbit * zbit)
  addbit <<= 1
  zwire += 1

print(result)
