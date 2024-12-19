import heapq

with open('17.txt') as f:
  starta = int(f.readline().removeprefix('Register A: '))
  startb = int(f.readline().removeprefix('Register B: '))
  startc = int(f.readline().removeprefix('Register C: '))
  f.readline()
  program = [int(o) for o in f.readline().strip().removeprefix('Program: ').split(',')]


def runprogram(program, a, b, c):
  def combo(n):
    match n:
      case c if c <= 3: return c
      case 4: return a
      case 5: return b
      case 6: return c
      case _: raise ValueError

  pc = 0

  outs = []
  while True:
    match program[pc:pc+2]:
      case [] | [_]:
        break
      case [0, cn]:  # adv
        a = a // (2 ** combo(cn))
      case [1, ln]:  # bxl
        b = b ^ ln
      case [2, cn]:  # bst
        b = combo(cn) & 0x7
      case [3, ln]:  # jnz
        if a != 0:
          pc = ln
          continue
      case [4, _]:  # bxc
        b = b ^ c
      case [5, cn]:  # out
        outs.append(combo(cn) & 0x7)
      case [6, cn]:  # bdv
        b = a // (2 ** combo(cn))
      case [7, cn]:  # cdv
        c = a // (2 ** combo(cn))
    
    pc += 2

  return outs


# part 1

print(','.join([str(x) for x in runprogram(program, starta, startb, startc)]))

# part 2

candidates = [0]

while len(candidates) > 0:
  c = heapq.heappop(candidates)
  for newa in range(c, c+8):
    o = runprogram(program, newa, startb, startc)

    if o == program:
      print(newa)
      candidates.clear()
    elif program[-len(o):] == o:
      heapq.heappush(candidates, newa * 8)
