lines = list(open("input.txt").readlines())

max_calories = 0
elf_calories = 0

for line in lines:
    if line == '\n':
        max_calories = max(max_calories, elf_calories)
        elf_calories = 0
        continue

    elf_calories += int(line)

print("part 1: ", max_calories)

# Part 2

elf_calories = 0
elf_calories_list = []

for line in lines:
    if line == '\n':
        elf_calories_list.append(elf_calories)
        elf_calories = 0
        continue

    elf_calories += int(line)

top3 = list(reversed(sorted(elf_calories_list)))[:3]

print("part 2: ", sum(top3))
