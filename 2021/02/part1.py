lines = list(open("input.txt").readlines())

horizontal_position = 0
depth = 0

for line in lines:
    (operation, magnitude) = line.split(" ")
    if operation == 'forward':
        horizontal_position += int(magnitude)
    if operation == 'up':
        depth -= int(magnitude)
    if operation == 'down':
        depth += int(magnitude)

print("horizontal position: ", horizontal_position)
print("depth: ", depth)
print("answer", horizontal_position * depth)
