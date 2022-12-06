stream = open('input.txt').read()

processed_characters = 3

for i in range(0, len(stream) - 3):
    processed_characters += 1
    four_previous = stream[i:(i+4)]
    if len(set(list(four_previous))) == 4:
        break

print("part 1: ", processed_characters)

processed_characters = 13

for i in range(0, len(stream) - 12):
    processed_characters += 1
    fourteen_previous = stream[i:(i+14)]
    if len(set(list(fourteen_previous))) == 14:
        break

print("part 2: ", processed_characters)
