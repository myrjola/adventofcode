# lanternfish = list(map(int, open("test-input.txt", 'r').readline().strip().split(',')))
lanternfish = list(map(int, open("input.txt", 'r').readline().strip().split(',')))

reset_fish = 6
new_fish = 8

def simulate(lanternfishlist):
    result = []
    for fish in lanternfishlist:
        if fish == 0:
            result.append(reset_fish)
            result.append(new_fish)
        else:
            result.append(fish - 1)
    return result

part1 = lanternfish

for day in range(80):
    part1 = simulate(part1)

print("Part 1: ", len(part1))

# Part 2 seems to explode in complexity. Let's try to be more effective.

fishdict = dict.fromkeys(range(9), 0)
for fish in lanternfish:
    fishdict[fish] += 1

def simulate(lanternfishdict):
    result = dict.fromkeys(range(9), 0)
    for age, fish_count in lanternfishdict.items():
        if age == 0:
            result[reset_fish] += fish_count
            result[new_fish] += fish_count
        else:
            result[age - 1] += fish_count
    return result

for day in range(256):
    fishdict = simulate(fishdict)

print("Part 2:", sum(fishdict.values()))
