
crabs = list(map(int, open("input.txt", 'r').readline().strip().split(',')))

fuel_costs = [sum([abs(crab - position) for crab in crabs]) for position in range(max(crabs))]

# plot the fuel costs
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(range(len(fuel_costs)), fuel_costs)

print('part 1: ', min(fuel_costs))
