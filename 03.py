import re

with open('inputs/03.txt') as f:
  contents = f.read()

total = 0
total_with_conditionals = 0
adding = True

# https://regex101.com/r/uUZVHU/1
r = re.compile(r'''(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))''')
for m in r.finditer(contents):
  if m[0] == 'do()':
    adding = True
  elif m[0] == '''don't()''':
    adding = False
  else:
    n = int(m[2]) * int(m[3])
    total += n
    if adding:
      total_with_conditionals += n

# part 1
print(total)

# part 2
print(total_with_conditionals)
