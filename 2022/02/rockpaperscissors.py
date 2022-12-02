lines = list(open("input.txt").readlines())

score = 0

for line in lines:
    opponent, me = line.strip().split(' ')

    if me == 'X':
        score += 1
        if opponent == 'A':
            score += 3
        if opponent == 'B':
            score += 0
        if opponent == 'C':
            score += 6

    if me == 'Y':
        score += 2
        if opponent == 'A':
            score += 6
        if opponent == 'B':
            score += 3
        if opponent == 'C':
            score += 0

    if me == 'Z':
        score += 3
        if opponent == 'A':
            score += 0
        if opponent == 'B':
            score += 6
        if opponent == 'C':
            score += 3

print("part1: ", score)

score = 0

for line in lines:
    opponent, me = line.strip().split(' ')

    if me == 'X':
        if opponent == 'A':
            score += 3
        if opponent == 'B':
            score += 1
        if opponent == 'C':
            score += 2

    if me == 'Y':
        if opponent == 'A':
            score += 4
        if opponent == 'B':
            score += 5
        if opponent == 'C':
            score += 6

    if me == 'Z':
        if opponent == 'A':
            score += 8
        if opponent == 'B':
            score += 9
        if opponent == 'C':
            score += 7

print("part2: ", score)
