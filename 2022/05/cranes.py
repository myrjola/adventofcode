import itertools
import collections

crates_section, moves_section = open('input.txt').read().split('\n\n')

# Parse columns
crates_grid = crates_section.split('\n')[:-1]
rows = [row[1::4] for row in crates_grid]
columns = [collections.deque(filter(lambda s: s != ' ', column)) for column in itertools.zip_longest(*rows, fillvalue=' ')]

moves = moves_section.split('\n')[:-1]

for move in moves:
    amount, from_spot, to_spot = map(int, move.split()[1::2])

    # move crates
    for i in range(amount):
        crate = columns[from_spot - 1].popleft()
        columns[to_spot - 1].appendleft(crate)

print("part 1:",  ''.join(list(zip(*columns))[0]))

columns = [collections.deque(filter(lambda s: s != ' ', column)) for column in itertools.zip_longest(*rows, fillvalue=' ')]

for move in moves:
    amount, from_spot, to_spot = map(int, move.split()[1::2])

    # move crates
    crates = []
    for i in range(amount):
        crates.append(columns[from_spot - 1].popleft())

    columns[to_spot - 1].extendleft(reversed(crates))

print("part 2:",  ''.join(list(zip(*columns))[0]))
