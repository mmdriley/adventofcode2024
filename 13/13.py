# a machine is defined by:
# A+X, A+Y, B+X, B+Y, prize.X, prize.Y

import re

with open('13.txt') as f:
  machine_descriptions = f.read()

machine_regex = re.compile(r"""
Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)""".lstrip())

machines = []

for m in machine_regex.finditer(machine_descriptions):
  machines.append(tuple(int(k) for k in m.groups()[0:7]))


# pressing A costs three tokens; pressing B costs one token

def spend_or_zero(ax, ay, bx, by, prizeX, prizeY):
  # use Cramer's rule to solve a system of two linear equations
  detA = (ax * by) - (bx * ay)
  detA1 = (prizeX * by) - (bx * prizeY)
  detA2 = (ax * prizeY) - (prizeX * ay)

  n = detA1 / detA
  k = detA2 / detA

  # no solution if it would require a fractional number of button presses
  if n != int(n) or k != int(k):
    return 0

  return int(3*n + 1*k)


# part 1

spend1 = 0
for ax, ay, bx, by, prizeX, prizeY in machines:
  spend1 += spend_or_zero(ax, ay, bx, by, prizeX, prizeY)

print(spend1)


# part 2

spend2 = 0
for ax, ay, bx, by, prizeX, prizeY in machines:
  spend2 += spend_or_zero(ax, ay, bx, by,
                          prizeX + 10000000000000, prizeY + 10000000000000)

print(spend2)
