import sys
import traceback

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
  

def evalwire(wire: str) -> int:
  if wire in startwires:
    return startwires[wire]
  
  if wire in gates:
    (w1, op, w2) = gates[wire]
    w1val = evalwire(w1)
    w2val = evalwire(w2)

    match op:
      case 'AND':
        return w1val & w2val
      case 'OR':
        return w1val | w2val
      case 'XOR':
        return w1val ^ w2val

  raise ValueError


# starts z00
zwires = sorted([w for w in gates if w.startswith('z')])
assert(int(zwires[-1][1:]) == len(zwires) - 1)

# part 1

result = 0

for zwire in reversed(zwires):
  zbit = evalwire(zwire)
  result = result << 1 | zbit

print(result)


# part 2

#
# full adder:
#   xor1 = x00 xor y00
#   and1 = x00 and y00
#   z00 = xor2 = xor1 xor carryin
#   and2 = xor1 and carryin
#   carryout = or1 = and1 or and2
#

# cbj,cfk,dmn,gmt,qjj,z07,z18,z35
gates['dmn'], gates['z18'] = gates['z18'], gates['dmn']
gates['gmt'], gates['z07'] = gates['z07'], gates['gmt']
gates['cfk'], gates['z35'] = gates['z35'], gates['cfk']
gates['qjj'], gates['cbj'] = gates['cbj'], gates['qjj']

def expect_eq(lhs: str, rhs: str):
  if lhs == rhs:
    return
  print(lhs, '!=', rhs)
  traceback.print_stack(limit=3, file=sys.stdout)


# input1, op -> input2, output
gateindex: dict[tuple[str, str], tuple[str, str]] = dict()

for (w3, (w1, op, w2)) in gates.items():
  assert((w1, op) not in gateindex)
  gateindex[(w1, op)] = (w2, w3)

  assert((w2, op) not in gateindex)
  gateindex[(w2, op)] = (w1, w3)


# find first half-adder and identify carry out
assert(gateindex[('x00', 'XOR')] == ('y00', 'z00'))
(w1, w3) = gateindex[('x00', 'AND')]
assert(w1 == 'y00')
carry = w3

# leave out first+last for special handling
for zwire in zwires[1:-1]:
  try:
    print(zwire)

    xwire = 'x' + zwire[1:]
    ywire = 'y' + zwire[1:]

    (other, and1output) = gateindex[(xwire, 'AND')]
    expect_eq(other, ywire)
    print('  and1: ' + and1output)
    (other, xor1output) = gateindex[(xwire, 'XOR')]
    expect_eq(other, ywire)
    print('  xor1: ' + xor1output)

    (carryin, out) = gateindex[(xor1output, 'XOR')]
    print('  carryin: ' + carryin)
    expect_eq(out, zwire)
    expect_eq(carryin, carry)

    (other, and2output) = gateindex[(xor1output, 'AND')]
    expect_eq(other, carryin)
    print('  and2: ' + and2output)

    (other, carryout) = gateindex[(and1output, 'OR')]
    print('  carryout: ' + carryout)
    expect_eq(other, and2output)

    (w1, op, w2) = gates[other]
    expect_eq(op, 'AND')
    if w2 == carryin:
      w1, w2 = w2, w1
    assert(w1 == carryin)
    assert(w2 == xor1output)

    carry = carryout

  except KeyError:
    traceback.print_exc(file=sys.stdout)

  # now look up from Z

  (w1, op, w2) = gates[zwire]
  expect_eq(op, 'XOR')

expect_eq(carry, zwires[-1])
