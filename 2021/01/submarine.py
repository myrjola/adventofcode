with open("submarine.txt", "r") as file:
    depths = []
    for line in file:
        depths.append(float(line))

    summed_windows = []
    for start in range(len(depths)-2):
        summed_windows.append(sum(depths[start:start+3]))

    prev_sum = summed_windows[0]
    larger_than_prev = 0
    for summed_window in summed_windows[1:]:
        if (summed_window > prev_sum):
            larger_than_prev += 1
        prev_sum = summed_window

    print(larger_than_prev)
