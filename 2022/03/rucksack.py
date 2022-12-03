lines = list(open("input.txt").readlines())

def get_priority(char):
    if char.islower():
        return ord(char) - 96
    if char.isupper():
        return ord(char) - 38

priority_sum = 0

for line in lines:
    line = line.strip()
    half = len(line) // 2
    first = set(list(line[:half]))
    second = set(list(line[half:]))
    common = first.intersection(second)
    priority_sum += sum([get_priority(item) for item in common])

print("part 1: ", priority_sum)

priority_sum = 0

for i in range(0, len(lines), 3):
    first = set(list(lines[i].strip()))
    second = set(list(lines[i+1].strip()))
    third = set(list(lines[i+2].strip()))
    common = first.intersection(second.intersection(third))
    priority_sum += sum([get_priority(item) for item in common])

print("part 2: ", priority_sum)
