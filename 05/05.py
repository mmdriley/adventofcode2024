from functools import cmp_to_key


rules: list[tuple[int, int]] = []
updates: list[list[int]] = []


with open('05.txt') as f:
  for l in f:
    if l == '\n':
      break
    (before, after) = l.strip().split('|')
    rules += [(int(before), int(after))]

  for l in f:
    updates += [[int(x) for x in l.strip().split(',')]]


def sortfn(lhs: int, rhs: int) -> int:
  if lhs == rhs:
    return 0
  if (lhs, rhs) in rules:
    return -1
  if (rhs, lhs) in rules:
    return 1
  raise ValueError()


correct_sum = 0
incorrect_sum = 0
for u in updates:
  sortedu = sorted(u, key=cmp_to_key(sortfn))
  middle = sortedu[len(sortedu)//2]

  if u == sortedu:
    correct_sum += middle
  else:
    incorrect_sum += middle


# part 1

print(correct_sum)

# part 2

print(incorrect_sum)


# ABANDONED: naive part 1
#
# correct_updates: list[list[int]] = []
# for u in updates:
#   for (before, after) in rules:
#     try:
#       if u.index(before) > u.index(after):
#         incorrect_updates.append(u)
#         break
#     except ValueError:
#       # rule doesn't apply
#       continue
#   else:
#     correct_updates.append(u)
