with open("submarine.txt", "r") as file:
    prev = float('inf')
    larger_than_prev = 0
    for line in file:
        if float(line) > prev:
            larger_than_prev += 1
        prev = float(line)
    print(larger_than_prev)

