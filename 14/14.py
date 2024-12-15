import re

robot_re = re.compile(
  r'''^p=(\d+),(\d+) v=(-?\d+),(-?\d+)$''')

# startX, startY, vX, vY
Robot = tuple[int, int, int, int]
robots: list[Robot] = []

with open('14.txt') as f:
  for l in f:
    m = robot_re.match(l)
    assert(m)
    robots.append(tuple(int(i) for i in m.group(1, 2, 3, 4)))  # type: ignore

# grid is 101 tiles wide, 103 tiles tall
grid_w = 101
grid_h = 103

# part 1

mid_w = grid_w // 2
mid_h = grid_h // 2

iter_seconds = 100

robots_after: list[tuple[int, int]] = []
for start_x, start_y, v_x, v_y in robots:
  end_x = (start_x + v_x * iter_seconds) % grid_w
  end_y = (start_y + v_y * iter_seconds) % grid_h

  robots_after.append((end_x, end_y))

quadrant_counts = [0, 0, 0, 0]
for end_x, end_y in robots_after:
  if end_x == mid_w or end_y == mid_h:
    continue
  q = 0
  if end_x > mid_w:
    q += 1
  if end_y > mid_h:
    q += 2
  quadrant_counts[q] += 1

p = 1
for c in quadrant_counts:
  p *= c
print(p)

# part 2

robots_now = robots.copy()

screen = ([' '] * grid_w + ['\n']) * grid_h
for currentX, currentY, _, _ in robots_now:
  screen[(currentY * (grid_w + 1)) + currentX] = '#'

seconds = 0
while seconds < 10000:
  # first solved by visual inspection in VSCode codemap...
  #
  # with open('14tree.txt', 'a') as f:
  #   print(''.join(screen), file=f)
  #   print(seconds, file=f)

  screenstr = ''.join(screen)
  if screenstr.find('########') >= 0:
    print(seconds)
    break

  for i in range(len(robots_now)):
    currentX, currentY, dX, dY = robots_now[i]

    screen[(currentY * (grid_w + 1)) + currentX] = ' '
    
    currentX = (currentX + dX) % grid_w
    currentY = (currentY + dY) % grid_h

    screen[(currentY * (grid_w + 1)) + currentX] = '#'

    robots_now[i] = currentX, currentY, dX, dY

  seconds += 1
