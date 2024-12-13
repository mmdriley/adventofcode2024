# a machine is defined by:
# A+X, A+Y, B+X, B+Y, prize.X, prize.Y

from functools import cache
import re

with open('13.txt') as f:
  machine_descriptions = f.read()

machine_regex = re.compile(
  r"""Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)""")

machines = []

for m in machine_regex.finditer(machine_descriptions):
  machines.append(tuple(int(k) for k in m.groups()[0:7]))


impossible_sentinel = -2, -2


def cost(solve: tuple[int, int]) -> int:
  n_a, n_b = solve
  return 3 * n_a + 1 * n_b


# returns A presses, B presses
@cache
def mincostsolve(ax, ay, bx, by, prizeX, prizeY, max_presses) -> tuple[int, int]:
  if max_presses <= 0:
    return impossible_sentinel

  if prizeX < 0 or prizeY < 0:
    return impossible_sentinel

  if prizeX == 0 and prizeY == 0:
    return 0, 0
  
  solve_a = solve_b = impossible_sentinel

  aa, ab = mincostsolve(ax, ay, bx, by, prizeX - ax, prizeY - ay, max_presses - 1)
  if aa < max_presses and ab >= 0:
    solve_a = (aa + 1, ab)

  ba, bb = mincostsolve(ax, ay, bx, by, prizeX - bx, prizeY - by, max_presses - 1)
  if bb < max_presses and ba >= 0:
    solve_b = (ba, bb + 1)

  if solve_a == impossible_sentinel:
    return solve_b
  elif solve_b == impossible_sentinel:
    return solve_a
  else:
    return solve_a if cost(solve_a) < cost(solve_b) else solve_b


# part 1

spend1 = 0
for ax, ay, bx, by, prizeX, prizeY in machines:
  sa, sb = mincostsolve(ax, ay, bx, by, prizeX, prizeY, 200)
  if sa >= 0:
    spend1 += cost((sa, sb))

    

print(spend1)
