import itertools

with open('inputs/04.txt') as f:
  wordsearch = f.readlines()

# surround with `#`
wordsearch = [f'#{l.strip()}#' for l in wordsearch]
dummyline = '#' * len(wordsearch[0])
wordsearch = [dummyline] + wordsearch + [dummyline]

# explode
wordsearch = [list(l) for l in wordsearch]

# part 1

moves = list(itertools.product(
  [-1, 0, 1],
  [-1, 0, 1]
))
moves.remove((0, 0))

word = 'XMAS'
wordsfound = 0

for i in range(1, len(wordsearch) - 1):
  for j in range(1, len(wordsearch[0]) - 1):
    if wordsearch[i][j] != word[0]:
      continue

    for (di, dj) in moves:
      for k in range(1, len(word)):
        (ii, jj) = (i + k * di, j + k * dj)
        if wordsearch[ii][jj] != word[k]:
          break
      else:
        wordsfound += 1

print(wordsfound)

# part 2

xmasfound = 0

for i in range(1, len(wordsearch) - 1):
  for j in range(1, len(wordsearch[0]) - 1):
    if wordsearch[i][j] != 'A':
      continue

    # recall indices increase *down* and *right*
    w1 = (
      wordsearch[i-1][j-1] +
      wordsearch[i][j] +
      wordsearch[i+1][j+1]
    )

    w2 = (
      wordsearch[i-1][j+1] +
      wordsearch[i][j] +
      wordsearch[i+1][j-1]
    )

    if (w1 == 'SAM' or w1 == 'MAS') and (w2 == 'SAM' or w2 == 'MAS'):
      xmasfound += 1

print(xmasfound)
