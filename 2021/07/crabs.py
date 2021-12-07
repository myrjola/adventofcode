crabs = list(map(int, open("input.txt", 'r').readline().strip().split(',')))

fuel_costs = [sum([abs(crab - position) for crab in crabs]) for position in range(max(crabs))]

print('part 1: ', min(fuel_costs))

def move(start, target):
    dist = abs(start - target)
    return sum(range(dist + 1))

fuel_costs_part2 = [sum([move(crab, position) for crab in crabs]) for position in range(max(crabs))]

print('part 2: ', min(fuel_costs_part2))

# plot the fuel costs
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(range(len(fuel_costs)), fuel_costs)
ax.plot(range(len(fuel_costs_part2)), fuel_costs_part2)
